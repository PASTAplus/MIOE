#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: access

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
logger = logging.getLogger('access')

import json

class Rule(object):

    def __init__(self, principal=None, permission=None):
        self.principal = principal
        self.permission = permission

    def to_json(self):
        return json.dumps({'principal': self.principal,
                           'permission': self.permission})

    @staticmethod
    def from_json(rule='null'):
        return json.loads(rule)


class Access(object):

    def __init__(self):
        self.deny_rules = []
        self.allow_rules = []
        self.rules = 0

    def rule_count(self):
        return  self.rules

    def add_allow_rule(self, principal='public', permission='read'):
        self.allow_rules.append(Rule(principal, permission))
        self.rules += 1

    def add_deny_rule(self, principal='public', permission='read'):
        self.deny_rules.append(Rule(principal, permission))
        self.rules += 1

    def remove_allow_rule(self, principal='public', permission='read'):
        rule = Rule(principal, permission)
        try:
            self.allow_rules.remove(rule)
            self.rules -= 1
        except ValueError:
            logger.warn('Attempting to remove allow rule that does not exist')

    def remove_deny_rule(self, principal='public', permission='read'):
        rule = Rule(principal, permission)
        try:
            self.deny_rules.remove(rule)
            self.rules -= 1
        except ValueError:
            logger.warn('Attempting to remove deny rule that does not exist')

    def to_json(self):
        # TODO: decide how to handle an empty access element
        pass




def main():
    return 0


if __name__ == "__main__":
    main()