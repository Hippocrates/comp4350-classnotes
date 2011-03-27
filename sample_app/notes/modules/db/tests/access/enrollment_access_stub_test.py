import unittest
from ....logic.objects.enrollment import Enrollment
from ...access.enrollments_stub import EnrollmentsAccessorStub

class EnrollmentAccessStubTest(unittest.TestCase):
    def setUp(self):
        self.access_enrollment = EnrollmentsAccessorStub()

    def testConstructor(self):
        assert self.access_enrollment is not None


    def testInsertEnrollment(self):
        count1 = len(self.access_enrollment.get_user_enrollments(10))
        assert self.access_enrollment.insert_enrollment(Enrollment(10, 10)) > 0
        count2 = len(self.access_enrollment.get_user_enrollments(10))
        assert count2 > count1


    def testDeleteEnrollment(self):
        assert self.access_enrollment.delete_enrollment(1)

    def testUserEnrollments(self):
        assert len(self.access_enrollment.get_user_enrollments(1)) > 0

    @staticmethod
    def suite():
        suite = unittest.TestSuite()
        suite = unittest.TestLoader().loadTestsFromTestCase(EnrollmentAccessStubTest);
        return suite
