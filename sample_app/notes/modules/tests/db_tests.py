# To run this application, you need to run it from inside web2py.
# hence, with your current directory in the 'web2py' folder, run
# this command:
# > python web2py.py -S notes -M -R applications/notes/modules/tests/db_tests.py

import unittest

import os
import glob

from datetime import datetime, date
from gluon.dal import DAL
from gluon.contrib.populate import populate

from applications.notes.modules.db.access.courses import CoursesAccessor
from applications.notes.modules.db.access.notes import NotesAccessor

class TestContext(DBContext):
    """ Class to handle setting up / destroying test database context """

    @staticmethod
    def begin():
        """ called at the beginning of a test """
        TestContext.db_context = DBContext("test.sqlite", lambda table: "%s.test.migrate" % table)
        db = TestContext.db_context.db

        # populate test database with dummy data
        populate(db.courses, 100)
        populate(db.notes, 100)

    @staticmethod
    def end():
      """ called at the end of a test """
      #delete migration files and test database file
      path_to_db = os.path.join(os.getcwd(), 'applications', 'notes', 'databases')
      TestContext.db_context.close()
      os.unlink(os.path.join(path_to_db, TestContext.db_context.db_file))

      migrate_files = glob.glob(os.path.join(path_to_db, '*.test.migrate'))
      for file in migrate_files:
          os.unlink(file)

      TestContext.db_context = None


class CoursesAccessorTest(unittest.TestCase):
    def setUp(self):
        self.access_course = CoursesAccessor(TestContext.db_context)

    def testConstructor(self):
        assert self.access_course is not None

    def testCourseList(self):
        assert self.access_course.get_course_list().count > 50

    def testGetCourse(self):
        first = self.access_course.get_course_list()[0]
        assert self.access_course.get_course(first.id).id == first.id

    def testUpdateCourse(self):
        course = self.access_course.get_course_list()[0]
        assert course.dept != "TEST"
        course.dept = "TEST"
        assert self.access_course.update_course(course)
        assert self.access_course.get_course(course.id).dept == "TEST"

    def testInsertCourse(self):
        count1 = len(self.access_course.get_course_list())
        self.access_course.insert_course(Course("TEST", "2020", "A02", "Zapp"))
        count2 = len(self.access_course.get_course_list())
        assert count2 > count1


    def testDeleteCourse(self):
        assert self.access_course.get_course(1) is not None
        assert self.access_course.delete_course(1)
        assert self.access_course.get_course(1) is None

class NotesAccessorTest(unittest.TestCase):
    def setUp(self):
        self.access_note = NotesAccessor(TestContext.db_context)

    def testConstructor(self):
        assert self.access_note is not None

    def testNoteList(self):
        assert self.access_note.get_note_list().count > 50

    def testGetNote(self):
        first = self.access_note.get_note_list()[0]
        assert self.access_note.get_note(first.id).id == first.id

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
        course_notes = self.access_note.get_course_notes(self.access_note.get_note_list()[0].course_id)
        all_notes = self.access_note.get_note_list()
        assert len(course_notes) > 0
        assert len(course_notes) < len(all_notes)

def run(suite_class):
    print "Running ", suite_class
    TestContext.begin()
    suite = unittest.TestLoader().loadTestsFromTestCase(suite_class);
    runner = unittest.TextTestRunner()
    runner.run(suite)
    TestContext.end()
    print "-" * 20

# entry point
def main():
    run(CoursesAccessorTest)
    run(NotesAccessorTest)


# run main
main()
