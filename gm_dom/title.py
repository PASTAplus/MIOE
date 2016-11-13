#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: title

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
logger = logging.getLogger('title')


import json

class Title(object):

    def __init__(self, title=None):
        self.title = title

def main():
    return 0


if __name__ == "__main__":
    main()