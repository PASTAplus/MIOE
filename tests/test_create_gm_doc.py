#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: test_create_gm_doc

:Synopsis:

:Author:
    servilla
  
:Created:
    10/21/16
"""

import unittest
import logging

logging.basicConfig(format='%(asctime)s %(levelname)s (%(name)s): %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S%z')
logging.getLogger('').setLevel(logging.WARN)
logger = logging.getLogger('test_create_gm_doc')

from .context import gm_dom

class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
