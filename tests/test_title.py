#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: test_title

:Synopsis:

:Author:
    servilla
  
:Created:
    11/12/16
"""

import unittest
import logging

logging.basicConfig(format='%(asctime)s %(levelname)s (%(name)s): %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S%z')
logging.getLogger('').setLevel(logging.WARN)
logger = logging.getLogger('test_title')

import json

from .context import title


class TestTitle(unittest.TestCase):
    test_title = "This is a test title!"
    json_title = json.dumps({'title': test_title})

    def setUp(self):
        self.title = title.Title(TestTitle.test_title)

    def tearDown(self):
        pass

    def test_default_title(self):
        self.assertEquals(TestTitle.test_title, self.title.get_title(),
                          msg='{test}: expected title "{title}", but received "{error}"'.format(
                              test='test_title', title=TestTitle.test_title,
                              error=self.title.get_title()))

    def test_to_json(self):
        json_title = self.title.to_json()
        self.assertEquals(TestTitle.json_title, json_title)


if __name__ == '__main__':
    unittest.main()
