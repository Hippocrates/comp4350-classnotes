from ...search.submit_note import SubmitNote
from ....db.access.course_stub import CourseAccessorStub
from ....db.access.note_stub import NoteAccessorStub
from ....db.access.users_stub import UsersAccessorStub
from ....db.access.enrollments_stub import EnrollmentsAccessorStub

from datetime import date

import unittest;

class DummyFileUpload:
    def __init__(self, file, filename):
        self.file = file;
        self.filename = filename;

class SubmitNoteTest(unittest.TestCase):
    def setUp(self):
        self.access_course = CourseAccessorStub();
        self.access_note = NoteAccessorStub()
        self.access_user = UsersAccessorStub();
        self.access_enrollment = EnrollmentsAccessorStub();
        self.submiter = SubmitNote(self.access_course, self.access_note, self.access_user, self.access_enrollment);

    def testSubmit(self):
        department = "COMP";
        number = "1010";
        section = "A01";
        startDate = date(2011, 01, 01);
        endDate = date(2011, 01, 03);
        userId = 3;
        filename = "some_fake_file.pdf";
        fileObject = DummyFileUpload(None, filename);
        submit_result = self.submiter.submit_note(
            startDate, endDate, fileObject, userId,
            department, number, section );
        self.assertTrue(submit_result != None);
        note = self.access_note.get_note(submit_result);

    def testSubmitImplicitSection(self):
        department = "COMP";
        number = "1010";
        startDate = date(2011, 01, 01);
        endDate = date(2011, 01, 03);
        userId = 3;
        filename = "some_fake_file.pdf";
        fileObject = DummyFileUpload(None, filename);
        submit_result = self.submiter.submit_note(
            startDate, endDate, fileObject, userId,
            department, number);
        self.assertTrue(submit_result != None);
        note = self.access_note.get_note(submit_result);

    def testBadSubmitNoCourse(self):
        department = "FAKE";
        number = "1234";
        section = "A01";
        startDate = date(2011, 01, 01);
        endDate = date(2011, 01, 03);
        userId = 1;
        filename = "some_fake_file.pdf";
        fileObject = DummyFileUpload(None, filename);
        submit_result = self.submiter.submit_note(
            startDate, endDate, fileObject, userId,
            department, number, section );
        self.assertTrue(submit_result == None);

    @staticmethod
    def suite():
        suite = unittest.TestSuite()
        suite.addTest(SubmitNoteTest("testSubmit"));
        suite.addTest(SubmitNoteTest("testSubmitImplicitSection"));
        suite.addTest(SubmitNoteTest("testBadSubmitNoCourse"));
        return suite
