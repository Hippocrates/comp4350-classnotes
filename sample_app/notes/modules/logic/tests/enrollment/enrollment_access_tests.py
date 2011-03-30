import unittest
from ...objects.enrollment import Enrollment
from ...enrollment.enrollment_access import EnrollmentAccess
from ....db.access.enrollments_stub import EnrollmentsAccessorStub

class EnrollmentAccessTest(unittest.TestCase):
    def setUp(self):
        self.access_enrollment = EnrollmentsAccessorStub()
        self.enrollment_access = EnrollmentAccess(self.access_enrollment)

    def testConstructor(self):
        assert self.enrollment_access is not None


    def testInsertEnrollment(self):
        count1 = len(self.enrollment_access.get_user_enrollments(10))
        assert self.enrollment_access.insert_enrollment(10, 10) > 0
        count2 = len(self.enrollment_access.get_user_enrollments(10))
        assert count2 > count1


    def testDeleteEnrollment(self):
        assert self.enrollment_access.delete_enrollment(1)

    def testUserEnrollments(self):
        assert len(self.enrollment_access.get_user_enrollments(1)) > 0

    @staticmethod
    def suite():
        suite = unittest.TestSuite()
        suite = unittest.TestLoader().loadTestsFromTestCase(EnrollmentAccessTest);
        return suite
