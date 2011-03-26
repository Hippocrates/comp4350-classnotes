import unittest
from ....logic.objects.note import Note
from ...access.note_stub import NoteAccessorStub
from datetime import date

class NoteAccessStubTest(unittest.TestCase):
    def setUp(self):
        self.access_note = NoteAccessorStub()

    def testConstructor(self):
        assert self.access_note is not None

    def testNoteList(self):
        assert self.access_note.get_note_list().count > 3

    def testGetNote(self):
        assert self.access_note.get_note(1).id == 1

    def testUpdateNote(self):
        note = self.access_note.get_note_list()[0]
        assert note.notes != "TEST"
        note.notes = "TEST"
        assert self.access_note.update_note(note)
        assert self.access_note.get_note(note.id).notes == "TEST"

    def testInsertNote(self):
        count1 = len(self.access_note.get_note_list())
        assert self.access_note.insert_note(Note(date(2011, 01, 01), date(2011, 01, 03), "testfile", 1, 1)) > 0
        count2 = len(self.access_note.get_note_list())
        assert count2 > count1


    def testDeleteNote(self):
        assert self.access_note.get_note(1) is not None
        assert self.access_note.delete_note(1)
        assert self.access_note.get_note(1) is None


    def testGetCourseNotes(self):
        course_notes = self.access_note.get_course_notes(1)
        all_notes = self.access_note.get_note_list()
        assert len(course_notes) > 0
        assert len(course_notes) < len(all_notes)

    @staticmethod
    def suite():
        suite = unittest.TestSuite()
        suite.addTest(NoteAccessStubTest("testConstructor"))
        suite.addTest(NoteAccessStubTest("testNoteList"))
        suite.addTest(NoteAccessStubTest("testGetNote"))
        suite.addTest(NoteAccessStubTest("testUpdateNote"))
        suite.addTest(NoteAccessStubTest("testInsertNote"))
        suite.addTest(NoteAccessStubTest("testDeleteNote"))
        suite.addTest(NoteAccessStubTest("testGetCourseNotes"))
        return suite
