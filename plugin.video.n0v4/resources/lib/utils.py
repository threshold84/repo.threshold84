# -*- coding: utf-8 -*-

from __future__ import absolute_import

from tulip.cache import clear
from tulip.directory import resolve
from tulip.url_dispatcher import urldispatcher
from tulip.control import execute, refresh, sleep


@urldispatcher.register('play', ['url'])
def play(url):

    resolve(url)

    execute('PlayerControl(RepeatOne)')


@urldispatcher.register('cache_clear')
def cache_clear():

    clear(withyes=False, notify=False)
    sleep(200)
    refresh()
