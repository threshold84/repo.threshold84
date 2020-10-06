# -*- coding: utf-8 -*-

import re
from tulip import client, cache, directory, control
from tulip.parsers import itertags_wrapper
from tulip.url_dispatcher import urldispatcher
import concurrent.futures


def _get_content():

    _list = []
    result = []
    futures = []

    html = client.request('https://www.dailyiptvlist.com/european-m3u-iptv/greece-greek/')

    latest = itertags_wrapper(html, 'a', {'class': 'image-link'}, 'href')[0]

    nested = client.request(latest)

    playlists = itertags_wrapper(nested, 'a', {'href': '.+dailyiptvlist.com.+\.m3u'}, 'href')

    m3u = '\n'.join([client.request(i) for i in playlists])

    items = re.findall(r',(.+)$\r?\n(.+)', m3u, re.MULTILINE)

    for title, link in items:

        _list.append({'title': title[:-1], 'url': link[:-1]})

    with concurrent.futures.ThreadPoolExecutor(10) as executor:

        for i in _list:
            futures.append(executor.submit(_check_url, i))
        for future in concurrent.futures.as_completed(futures):
            item = future.result()
            if not item:
                continue
            result.append(item)

    return result


@urldispatcher.register('menu')
def menu():

    _list = cache.get(_get_content, 6)

    if _list is None:
        return

    cache_clear = {'title': 30001, 'query': {'action': 'cache_clear'}}

    for i in _list:
        i.update({'action': 'play', 'isFolder': 'False', 'cm': [cache_clear]})

    control.sortmethods('title')
    control.sortmethods()

    if control.setting('filter'):
        result = [i for i in _list if control.setting('filter').lower() in i['title'].lower()]
        directory.add(result)
    else:
        directory.add(_list)


def _check_url(item):

    try:
        ok = client.request(item['url'], output='response', timeout=10)[0] == u'200'
    except Exception:
        ok = False

    if ok:
        return item
    else:
        return
