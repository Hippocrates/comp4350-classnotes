import unittest

import objects.suite
import search.suite
import user_access.suite

def suite():
    # return the database test suite
    suite = unittest.TestSuite()

    # object tests
    suite.addTest(objects.suite.suite())
    # search tests
    suite.addTest(search.suite.suite())
    # user tests
    suite.addTest(user_access.suite.suite())

    return suite

