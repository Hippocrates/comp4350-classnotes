import unittest
from ...objects.course import Course

class CourseTest(unittest.TestCase):
    def testConstructor(self):
        course = Course(2, "Test", "Zapp")
        assert course.id == 2
        assert course.name == "Test"
        assert course.instructor == "Zapp"

    @staticmethod
    def suite():
        suite = unittest.TestSuite()
        suite.addTest(CourseTest("testConstructor"))
        return suite
