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

    def get_title(self):
        return self.title

    def set_title(self, title=None):
        self.title = title

    def trim_title(self):
        return self.title.strip()

    def to_json(self):
        return json.dumps({'title': self.title})

    @staticmethod
    def from_json(title='null'):
        return json.loads(title)


def main():
    return 0


if __name__ == "__main__":
    main()