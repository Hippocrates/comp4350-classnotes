import modules.db.tests.suite
import modules.logic.tests.suite
import unittest

# build a suite up of all the tests
suite = unittest.TestSuite()

suite.addTest(modules.db.tests.suite.suite()) # db tests
suite.addTest(modules.logic.tests.suite.suite())

# run the tests
runner = unittest.TextTestRunner()
runner.run(suite)
