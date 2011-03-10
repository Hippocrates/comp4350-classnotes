import unittest

from ...objects.course import Course
from ...objects.note import Note

class NoteTest(unittest.TestCase):
    def testConstructor(self):
        course = Course(1, "Test Course", "Zapp")
        note = Note(50, 'Jan5/2011', 'Jan7/2011', 'file', course,
                    'Josh', 'Jan8/2011', 'Josh', 'Jan8/2011')
        assert note.id == 50
        assert note.start_date == 'Jan5/2011'
        assert note.end_date == 'Jan7/2011'
        assert note.notes == 'file'
        assert note.course == course
        assert note.created_by == 'Josh'
        assert note.created_on == 'Jan8/2011'
        assert note.modified_by == 'Josh'
        assert note.modified_on == 'Jan8/2011'

    @staticmethod
    def suite():
        suite = unittest.TestSuite()
        suite.addTest(NoteTest("testConstructor"))
        return suite
