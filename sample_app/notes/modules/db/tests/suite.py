import unittest

import access.suite

def suite():
    # return the database test suite
    suite = unittest.TestSuite()

    # access tests
    suite.addTest(access.suite.suite())
    return suite

