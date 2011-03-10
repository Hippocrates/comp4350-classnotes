import unittest

import objects.suite

def suite():
    # return the database test suite
    suite = unittest.TestSuite()

    # for now just add object tests
    suite.addTest(objects.suite.suite())
    return suite

