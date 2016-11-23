#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: abstract

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
logger = logging.getLogger('abstract')


import json


class Abstract(object):

    def __init__(self, abstract=None):
        self.abstract = abstract

    def get_abstract(self):
        return self.abstract

    def set_abstract(self, abstract=None):
        self.abstract = abstract

    def trim_abstract(self):
        return self.abstract.strip()

    def to_json(self):
        return json.dumps({'abstract': self.abstract})

    @staticmethod
    def from_json(abstract='null'):
        return json.loads(abstract)


def main():
    return 0


if __name__ == "__main__":
    main()