import unittest
from ....logic.objects.user import User
from ...access.users_stub import UsersAccessorStub

class UserAccessStubTest(unittest.TestCase):
    def setUp(self):
        self.access_user = UsersAccessorStub()

    def testConstructor(self):
        assert self.access_user is not None

    def testUserList(self):
        assert self.access_user.get_user_list().count > 3

    def testGetUser(self):
        assert self.access_user.get_user(1).user_id == 1

    def testUpdateUser(self):
        user = self.access_user.get_user_list()[0]
        assert user.username != "TEST"
        user.username = "TEST"
        assert self.access_user.update_user(user)
        assert self.access_user.get_user(user.user_id).username == "TEST"

    def testInsertUser(self):
        count1 = len(self.access_user.get_user_list())
        self.access_user.insert_user(User("testy", User.ROLE_CONSUMER, "testy@gmail.com", "hash", "McTesterson", "Testy"))
        count2 = len(self.access_user.get_user_list())
        assert count2 > count1


    def testDeleteUser(self):
        assert self.access_user.get_user(1) is not None
        assert self.access_user.delete_user(1)
        assert self.access_user.get_user(1) is None

    @staticmethod
    def suite():
        suite = unittest.TestSuite()
        suite = unittest.TestLoader().loadTestsFromTestCase(UserAccessStubTest);
        return suite
