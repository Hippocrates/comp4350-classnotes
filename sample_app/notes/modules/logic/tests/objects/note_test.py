import unittest

from ...objects.note import Note

class NoteTest(unittest.TestCase):
    def setUp(self):
        self.note = Note('Jan5/2011', 'Jan7/2011', 'file', 1,
                    'Josh', 'Jan8/2011', 'Josh', 'Jan8/2011', 50)

    def testConstructor(self):
        assert self.note.id == 50
        assert self.note.start_date == 'Jan5/2011'
        assert self.note.end_date == 'Jan7/2011'
        assert self.note.notes == 'file'
        assert self.note.course_id == 1
        assert self.note.created_by == 'Josh'
        assert self.note.created_on == 'Jan8/2011'
        assert self.note.modified_by == 'Josh'
        assert self.note.modified_on == 'Jan8/2011'

    def testToString(self):
        str = "%s" % self.note
        assert str[0:4] == "Note"

    @staticmethod
    def suite():
        suite = unittest.TestSuite()
        suite.addTest(NoteTest("testConstructor"))
        suite.addTest(NoteTest("testToString"))
        return suite
