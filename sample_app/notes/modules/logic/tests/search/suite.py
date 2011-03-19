import unittest

from searcher_test import *
from submit_note_test import *

def suite():
    """ return the search test suite """
    suite = unittest.TestSuite()
    suite.addTest(SearcherTest.suite());
    suite.addTest(SubmitNoteTest.suite());
    return suite
