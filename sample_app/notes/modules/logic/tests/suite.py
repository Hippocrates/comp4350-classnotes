import unittest

import objects.suite

def suite():
    # return the database test suite
    suite = unittest.TestSuite()

    # object tests
    suite.addTest(objects.suite.suite())

    return suite

