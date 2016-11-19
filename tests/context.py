#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: context

:Synopsis:

:Author:
    servilla
  
:Created:
    11/12/16
"""

import logging

logging.basicConfig(format='%(asctime)s %(levelname)s (%(name)s): %(message)s',
                    datefmt='%Y-%m-%d% H:%M:%S%z')
logging.getLogger('').setLevel(logging.WARN)
logger = logging.getLogger('context')

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

from gm_dom import dom
from gm_dom import title

def main():
    return 0


if __name__ == "__main__":
    main()