import unittest
from ....logic.objects.course import Course
from ...access.course_stub import AccessCourseStub

class CourseAccessStubTest(unittest.TestCase):
    def setUp(self):
        self.access_course = AccessCourseStub()

    def testConstructor(self):
        assert self.access_course is not None

    def testCourseList(self):
        assert self.access_course.get_course_list().count > 3

    def testGetCourse(self):
        assert self.access_course.get_course(1).id == 1

    def testUpdateCourse(self):
        course = self.access_course.get_course_list()[0]
        assert course.dept != "TEST"
        course.dept = "TEST"
        assert self.access_course.update_course(course)
        assert self.access_course.get_course(course.id).dept == "TEST"

    def testInsertCourse(self):
        count1 = len(self.access_course.get_course_list())
        self.access_course.insert_course(Course("TEST", "2020", "A02", "Zapp"))
        count2 = len(self.access_course.get_course_list())
        assert count2 > count1


    def testDeleteCourse(self):
        assert self.access_course.get_course(1) is not None
        assert self.access_course.delete_course(1)
        assert self.access_course.get_course(1) is None

    @staticmethod
    def suite():
        suite = unittest.TestSuite()
        suite.addTest(CourseAccessStubTest("testConstructor"))
        suite.addTest(CourseAccessStubTest("testCourseList"))
        suite.addTest(CourseAccessStubTest("testGetCourse"))
        suite.addTest(CourseAccessStubTest("testUpdateCourse"))
        suite.addTest(CourseAccessStubTest("testInsertCourse"))
        suite.addTest(CourseAccessStubTest("testDeleteCourse"))
        return suite
