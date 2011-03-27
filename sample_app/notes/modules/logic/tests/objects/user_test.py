import unittest
from ...objects.user import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User('UMChris', 1, 'umjenkic@cc.umanitoba.ca', 'Secret', 'Jenkins', 'Chris', 50)
					

    def testConstructor(self):
        assert self.user.user_id == 50
        assert self.user.username == 'UMChris'
        assert self.user.email == 'umjenkic@cc.umanitoba.ca'
        assert self.user.password == 'Secret'
        assert self.user.last_name == 'Jenkins'
        assert self.user.first_name == 'Chris'

    def testToString(self):
        str = "%s" % self.user
        assert str == "User [user_id=50, email=umjenkic@cc.umanitoba.ca, lastName=Jenkins, firstName=Chris]"

    @staticmethod
    def suite():
        suite = unittest.TestSuite()
        suite.addTest(UserTest("testConstructor"))
        suite.addTest(UserTest("testToString"))
        return suite
