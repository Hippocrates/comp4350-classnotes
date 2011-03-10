import db.tests.suite
import unittest

# build a suite up of all the tests
suite = unittest.TestSuite()

suite.addTest(db.tests.suite.suite()) # db tests


# run the tests
runner = unittest.TextTestRunner()
runner.run(suite)
