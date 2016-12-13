#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: gm_dom

:Synopsis:

:Author:
    servilla
  
:Created:
    10/21/16
"""

import logging

logging.basicConfig(format='%(asctime)s %(levelname)s (%(name)s): %(message)s',
                    datefmt='%Y-%m-%d% H:%M:%S%z')
logging.getLogger('').setLevel(logging.WARN)
logger = logging.getLogger('gm_dom')


from gm_dom import access
from gm_dom import dataset


class GmDom(object):

    def __init__(self):
        self.dataset = dataset.Dataset()
        self.access = access.Access()


def main():
    return 0


if __name__ == "__main__":
    main()