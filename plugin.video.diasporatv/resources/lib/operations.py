# -*- coding: utf-8 -*-

'''
    Diaspora TV Addon
    Author Threshold84

        License summary below, for more details please read license.txt file

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 2 of the License, or
        (at your option) any later version.
        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.
        You should have received a copy of the GNU General Public License
        along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import json
from base64 import b64decode
from zlib import decompress
from os.path import join, exists as file_exists
from youtube_registration import register_api_keys

from tulip.url_dispatcher import urldispatcher
from tulip import directory, control
from tulip.log import log_debug

scramble = (
    'eJwVy80KgjAAAOBXkZ1LprNy3UqTQsoww25i25riz9RthkXvHt6/7wskIwNTYGuA6Ei5HnSlaEGKS+gdYLPfpH0MFgbIuzKr2DSz3emT3ya/eHj9M7'
    'sHNHG9MbkGdRzeZOoHTfTGfdKd51XSOVgQovUKYeza0FmWDkYN1ZwqS44jf3G7thiVTiFtUiGXm3nXSZMLwWumJRuIaBVrlUlEA35/OLI5KA=='
)


def enter_youtube():

    filepath = control.transPath(join(control.addon('plugin.video.youtube').getAddonInfo('profile'), 'api_keys.json'))

    setting = control.addon('plugin.video.youtube').getSetting('youtube.allow.dev.keys') == 'true'

    if file_exists(filepath):

        f = open(filepath)

        jsonstore = json.load(f)

        no_keys = 'plugin.video.diasporatv' not in jsonstore.get('keys', 'developer').get('developer')

        if setting and no_keys:

            yt_keys = json.loads(decompress(b64decode(scramble)))

            register_api_keys('plugin.video.diasporatv', yt_keys['api_key'], yt_keys['id'], yt_keys['secret'])
            log_debug('Successfully registered youtube keys')

        else:

            log_debug('Youtube keys have already been registered')

        f.close()


def android_activity(url, package=''):

    if package:
        package = '"' + package + '"'

    return xbmc.executebuiltin('StartAndroidActivity({0},"android.intent.action.VIEW","","{1}")'.format(package, url))


@urldispatcher.register('external', ['url'])
def open_web_browser(url):

    if control.condVisibility('system.platform.android'):

        return android_activity(url)

    else:

        import webbrowser

        return webbrowser.open(url)


@urldispatcher.register('play', ['url'])
def play(url):

    directory.resolve(url)


@urldispatcher.register('youtube', ['url'])
def yt(url):

    control.execute('Container.Update({},return)'.format(url))
