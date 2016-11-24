#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: test_access

:Synopsis:

:Author:
    servilla
  
:Created:
    11/23/16
"""

import unittest
import logging

logging.basicConfig(format='%(asctime)s %(levelname)s (%(name)s): %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S%z')
logging.getLogger('').setLevel(logging.WARN)
logger = logging.getLogger('test_access')

import json

from .context import access


class TestAccess(unittest.TestCase):

    principal = 'grinch'
    permission = 'write'
    test_rule = json.dumps({'principal': principal,
                           'permission': permission})

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_access_constructor(self):

        test_access = access.Access()
        rule_count = test_access.rule_count()
        msg = 'Expected: {empty}'.format(empty=0) + \
            'Received: {rule_count}'.format(rule_count=rule_count)
        self.assertEqual(0, rule_count, msg)

    def test_rule_to_json(self):

        rule = access.Rule(TestAccess.principal, TestAccess.permission)
        self.assertEqual(TestAccess.test_rule, rule.to_json())


if __name__ == '__main__':
    unittest.main()
