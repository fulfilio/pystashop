# -*- coding: utf-8 -*-
"""

    Tests

"""
import unittest
import doctest


def suite():
    suite = unittest.TestSuite()
    suite.addTests(doctest.DocFileSuite(
        '../mockstashop/tests/test_mockstashop.rst', encoding='utf-8',
        optionflags=doctest.REPORT_ONLY_FIRST_FAILURE)
    )
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
