import unittest

from course_access_stub_test import *
from note_access_stub_test import *
from user_access_stub_test import *
from enrollment_access_stub_test import *

def suite():
    """ return the access test suite """
    suite = unittest.TestSuite()
    suite.addTest(CourseAccessStubTest.suite())
    suite.addTest(NoteAccessStubTest.suite())
    suite.addTest(UserAccessStubTest.suite())
    suite.addTest(EnrollmentAccessStubTest.suite())
    return suite
