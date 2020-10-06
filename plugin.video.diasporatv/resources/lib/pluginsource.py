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

from os.path import join


def root():

    menu = [
        {
            'label': addon.get_localized_string(30001),
            'info': {'video': {'title': 'Diaspora TV'}},
            'url': plugin.get_url(action='play', url=video_url),
            'thumb': join(addon.path, 'icon.png'),
            'fanart': join(addon.path, 'fanart.jpg'),
            'is_playable': True,
            'stream_info': {'video': {'codec': 'h264'}},
            'is_folder': False
        }
        ,
        {
            'label': addon.get_localized_string(30002),
            'info': {'audio': {'title': 'Diaspora Radio'}},
            'url': plugin.get_url(action='play', url=radio_url),
            'thumb': join(addon.path, 'resources', 'media', 'radio_stream.jpg'),
            'fanart': join(addon.path, 'resources', 'media', 'radio_fanart.jpg'),
            'is_playable': True,
            'stream_info': {'audio': {'codec': 'mp3'}},
            'is_folder': False
        }
        ,
        {
            'label': addon.get_localized_string(30003),
            'url': plugin.get_url(plugin_url='plugin://plugin.video.youtube/channel/UCzmavZuisZ4a1DvHu8-6UwQ/?addon_id=plugin.video.ellinonsinelefis'),
            'thumb': join(addon.path, 'resources', 'media', 'youtube.jpg'),
            'fanart': join(addon.path, 'resources', 'media', 'youtube_fanart.jpg'),
            'is_folder': True,
            'is_playable': False
        }
        ,
        {
            'label': addon.get_localized_string(30004),
            'url': plugin.get_url(action='external'),
            'thumb': join(addon.path, 'resources', 'media', 'external.jpg'),
            'is_folder': True
        }
    ]



def play(params):

    yield params.url



def open_url(params):

    operations.open_web_browser(params.url)



def external():

    menu = [
        {
            'label': addon.get_localized_string(30005),
            'url': plugin.get_url(action='open_url', url='https://e-sy.gr/'),
            'thumb': join(addon.path, 'resources', 'media', 'esy_logo.jpg'),
            'is_folder': False,
            'is_playable': False
        }
    ]
