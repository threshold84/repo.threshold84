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

from kodi_six import xbmc
from simpleplugin import Addon
from youtube_registration import register_api_keys

yt_keys = {
    'id': '498788153161-pe356urhr0uu2m98od6f72k0vvcdsij0.apps.googleusercontent.com',
    'api_key': 'AIzaSyA8k1OyLGf03HBNl0byD511jr9cFWo2GR4',
    'secret': 'e6RBIFCVh1Fm-IX87PVJjgUu'
}

addon = Addon()


def enter_youtube():

    register_api_keys('plugin.video.ellinonsinelefis', yt_keys['api_key'], yt_keys['id'], yt_keys['secret'])
    addon.log('Successfully registered youtube keys')


def android_activity(url, package=''):

    if package:
        package = '"' + package + '"'

    return xbmc.executebuiltin('StartAndroidActivity({0},"android.intent.action.VIEW","","{1}")'.format(package, url))


def open_web_browser(url):

    if xbmc.getCondVisibility('system.platform.android'):

        return android_activity(url)

    else:

        import webbrowser

        return webbrowser.open(url)
