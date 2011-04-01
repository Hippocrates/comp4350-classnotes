from ....db.access.users_stub import UsersAccessorStub
from ....db.access.enrollments_stub import EnrollmentsAccessorStub
from ....db.access.course_stub import CourseAccessorStub
from ...objects.user import User
from ...user_access.user_control import UserControl
import unittest;


class UsersAccessTest(unittest.TestCase):
    def setUp(self):
        self.access_user = UsersAccessorStub();
        self.access_enrollements = EnrollmentsAccessorStub();
        self.access_course = CourseAccessorStub();
        self.user_control = UserControl(self.access_user);

    def testSubmitUser(self):
        username = 'umtester'
        email = 'umtester@cc.umanitoba.ca'
        password = 'secret'
        last_name = 'testerson'
        first_name = 'tester'
        role = User.ROLE_CONSUMER
        id = None
        id = self.user_control.insert_user(username,role,email,password,last_name,first_name)
        if id != None:
            returned_user = self.user_control.get_user(id)
            self.assertTrue(returned_user.username == username)
        

    def testUpdateUser(self):
        username = 'umtester'
        email = 'umtester@cc.umanitoba.ca'
        password = 'secret'
        last_name = 'testerson'
        first_name = 'tester'
        role = User.ROLE_CONSUMER
        id = None
        id = self.user_control.insert_user(username,role,email,password,last_name,first_name)
        self.assertTrue(id != None)
        user = self.user_control.get_user(id)
        self.assertTrue(user != None)
        user.username = 'umtester2'
        self.user_control.update_user(user)
        returned_user = self.user_control.get_user(id)
        self.assertTrue(returned_user.username == 'umtester2')

    def testDeleteUser(self):
        self.assertTrue(self.user_control.get_user(1) != None)
        self.assertTrue(self.user_control.delete_user(1))
        self.assertTrue(self.user_control.get_user(1) == None)


    @staticmethod
    def suite():
        suite = unittest.TestSuite()
        suite.addTest(UsersAccessTest("testSubmitUser"))
        suite.addTest(UsersAccessTest("testUpdateUser"))
        suite.addTest(UsersAccessTest("testDeleteUser"))
        return suite
