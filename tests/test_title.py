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
    py_title = json.loads(json_title)

    def setUp(self):
        self.title = title.Title(TestTitle.test_title)

    def tearDown(self):
        pass

    def test_default_title(self):
        test_title = self.title.get_title()
        msg = '{test}: expected title "{title}", but received "{error}"'.format(
            test='test_default_title', title=TestTitle.test_title,
            error=test_title)
        self.assertEquals(TestTitle.test_title, test_title, msg)

    def test_to_json(self):
        json_title = self.title.to_json()
        msg = '{test}: expected json "{json}", but received "{error}"'.format(
            test='test_to_json', json=TestTitle.json_title, error=json_title)
        self.assertEquals(TestTitle.json_title, json_title, msg)

    def test_from_json(self):
        py_title = self.title.from_json(TestTitle.json_title)
        msg = '{test}: expected object "{py}", but received "{error}"'.format(
            test='test_from_json', py=TestTitle.json_title, error=py_title)
        self.assertEqual(TestTitle.py_title, py_title, msg)


if __name__ == '__main__':
    unittest.main()
