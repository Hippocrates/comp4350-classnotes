import unittest

from course_test import *
from note_test import *

def suite():
    """ return the object test suite """
    suite = unittest.TestSuite()
    suite.addTest(CourseTest.suite())
    suite.addTest(NoteTest.suite())
    return suite
