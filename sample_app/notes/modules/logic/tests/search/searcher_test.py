from ...search.searcher import Searcher
from ...search.course_search_params import CourseSearchParams
from ...search.note_search_params import NoteSearchParams


from ....db.access.course_stub import CourseAccessorStub
from ....db.access.note_stub import NoteAccessorStub

import unittest;

class SearcherTest(unittest.TestCase):
    def setUp(self):
        self.access_course = CourseAccessorStub();
        self.access_note = NoteAccessorStub();
        self.seacher = Searcher(self.access_course, self.access_note);

    def testInstructorSearch(self):
        result = self.seacher.search_notes(CourseSearchParams(instructor='Braico'), NoteSearchParams());
        # only one course with this instructor
        self.assertEquals(1, len(result));
        for note in result:
            self.assertEquals('Braico', note.course.instructor);

    def testCourseSearch(self):
        result = self.seacher.search_courses(CourseSearchParams(department='COMP', number='2160'));
        # only one course with this id
        self.assertEquals(1, len(result));
        for course in result:
            self.assertEquals('COMP', course.dept);
            self.assertEquals('2160', course.number);

    @staticmethod
    def suite():
        suite = unittest.TestSuite()
        suite.addTest(SearcherTest("testInstructorSearch"));
        suite.addTest(SearcherTest("testCourseSearch"));
        return suite
