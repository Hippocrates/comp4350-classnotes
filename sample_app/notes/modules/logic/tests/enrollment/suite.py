import unittest

from enrollment_access_tests import *

def suite():
    """ return the enrollment access test suite """
    suite = unittest.TestSuite()
    suite.addTest(EnrollmentAccessTest.suite());
    return suite
