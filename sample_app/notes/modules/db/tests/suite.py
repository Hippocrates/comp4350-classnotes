import unittest

import objects.suite
import access.suite

def suite():
    # return the database test suite
    suite = unittest.TestSuite()

    # object tests
    suite.addTest(objects.suite.suite())

    # access tests
    suite.addTest(access.suite.suite())
    return suite

