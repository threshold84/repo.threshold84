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

import sys
from resources.lib import operations, pluginsource
from tulip.url_dispatcher import urldispatcher
from tulip.compat import parse_qsl

operations.enter_youtube()


def main(argv=None):

    if sys.argv:
        argv = sys.argv

    params = dict(parse_qsl(argv[2][1:]))
    action = params.get('action', 'root')
    urldispatcher.dispatch(action, params)


if __name__ == '__main__':

    sys.exit(main())
