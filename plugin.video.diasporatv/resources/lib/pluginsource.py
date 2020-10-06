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

video_url = 'https://itv.streams.ovh:443/diasporatv/diasporatv/playlist.m3u8'
radio_url = 'http://i3.streams.ovh:12119/stream'
channel_id = 'UCzmavZuisZ4a1DvHu8-6UwQ'

# rtmp://itv.streams.ovh:1935/diasporatv/diasporatv
# https://itv.streams.ovh:2000/l/?listen.diasporatv.m3u8
# https://e-sy.gr/
# https://www.youtube.com/channel/UC8Guqd2kE9-kL1R5ria-YBQ/
# https://www.youtube.com/channel/UCzmavZuisZ4a1DvHu8-6UwQ/
# https://www.youtube.com/channel/UCmeBnLE1wIeRsflFQQjmLnw/

from tulip import control, directory
from tulip.url_dispatcher import urldispatcher


@urldispatcher.register('root')
def root():

    menu = [
        {
            'label': control.lang(30001),
            'title': 'Diaspora TV',
            'url': video_url,
            'action': 'play',
            'isFolder': 'False'
        }
        ,
        {
            'label': control.lang(30002),
            'title': 'Diaspora Radio',
            'url': radio_url,
            'action': 'play',
            'isFolder': 'False',
            'icon': 'radio_stream.jpg',
            'fanart': control.join(control.addonInfo('path'), 'resources', 'media', 'radio_fanart.jpg')
        }
        ,
        {
            'title': control.lang(30003),
            'url': 'plugin://plugin.video.youtube/channel/UCzmavZuisZ4a1DvHu8-6UwQ/?addon_id=plugin.video.diasporatv',
            'action': 'youtube',
            'icon': 'youtube.jpg',
            'fanart': control.join(control.addonInfo('path'), 'resources', 'media', 'youtube_fanart.jpg'),
            'isFolder': 'False', 'isPlayable': 'False'
        }
        ,
        {
            'title': control.lang(30004),
            'action': 'external',
            'url': 'https://e-sy.gr/',
            'isFolder': 'False', 'isPlayable': 'False'
        }
    ]

    directory.add(menu)
