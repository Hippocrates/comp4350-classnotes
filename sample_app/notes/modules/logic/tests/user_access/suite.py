import unittest

from add_user_test import *

def suite():
    """ return the user test suite """
    suite = unittest.TestSuite()
    suite.addTest(UsersAccessTest.suite());
    return suite
