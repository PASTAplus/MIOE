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


class Access(object):

    def __init__(self, rule_type='allow', principal='public', permission='read'):
        """Access object constructor: requires at least one rule.

        :param (str) rule_type:
        :param (str) principal:
        :param (str) permission:
        """
        self.deny_rules = []
        self.allow_rules = []
        self.rules = 1

        if rule_type == 'allow':
            self.add_allow_rule(principal, permission)
        elif rule_type == 'deny':
            self.add_deny_rule(principal, permission)
        else:
            raise TypeError('Expected either "allow" or "deny" rule type, ' \
                            'but received {rule_type}'.format(rule_type=rule_type))

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
            if self.rules == 0:
                raise ValueError('Rule count cannot be zero!')
        except ValueError:
            logger.warn('Attempting to remove allow rule that does not exist')

    def remove_deny_rule(self, principal='public', permission='read'):
        rule = Rule(principal, permission)
        try:
            self.deny_rules.remove(rule)
            self.rules -= 1
            if self.rules == 0:
                raise ValueError('Rule count cannot be zero!')
        except ValueError:
            logger.warn('Attempting to remove deny rule that does not exist')



def main():
    return 0


if __name__ == "__main__":
    main()