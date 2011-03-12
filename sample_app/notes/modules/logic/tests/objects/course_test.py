import unittest
from ...objects.course import Course

class CourseTest(unittest.TestCase):
    def setUp(self):
        self.course = Course("COMP", "1010", "A01", "Zapp", 2)

    def testConstructor(self):
        assert self.course.id == 2
        assert self.course.dept == "COMP"
        assert self.course.number == "1010"
        assert self.course.section == "A01"
        assert self.course.instructor == "Zapp"

    def testToString(self):
        str = "%s" % self.course
        assert str == "COMP 1010 A01"

    @staticmethod
    def suite():
        suite = unittest.TestSuite()
        suite.addTest(CourseTest("testConstructor"))
        suite.addTest(CourseTest("testToString"))
        return suite
