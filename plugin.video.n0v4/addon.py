# -*- coding: utf-8 -*-

import sys
from resources.lib import lister, utils
from tulip.url_dispatcher import urldispatcher
from tulip.compat import parse_qsl


def main(argv=None):

    if sys.argv:
        argv = sys.argv

    params = dict(parse_qsl(argv[2][1:]))
    action = params.get('action', 'menu')
    urldispatcher.dispatch(action, params)


if __name__ == '__main__':

    sys.exit(main())
