#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: test_gm_dom

:Synopsis:

:Author:
    servilla
  
:Created:
    10/21/16
"""

import logging
import unittest

logging.basicConfig(format='%(asctime)s %(levelname)s (%(name)s): %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S%z')
logging.getLogger('').setLevel(logging.WARN)
logger = logging.getLogger('test_gm_dom')

from .context import dom


class TestGmDom(unittest.TestCase):

    def setUp(self):
        self.gm_dom = dom.GmDom()


    def tearDown(self):
        pass

    def test_create(self):
        pass


if __name__ == '__main__':
    unittest.main()
