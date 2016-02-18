# coding=utf-8

""""
Yatzy doctests for unittest
"""

import unittest
import doctest
import yatzy.yatzy


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(yatzy))
    return tests