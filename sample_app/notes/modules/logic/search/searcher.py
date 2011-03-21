from ..objects.note import Note
from ..objects.course import Course
import search;

class Searcher:
    def __init__(self, access_course, access_note):
        self.access_note = access_note;
        self.access_course = access_course;

    def search_courses(self, courseParams):
        course_list = self.access_course.get_course_list();
        return search.filter_course_list(course_list, courseParams);
		
    def search_notes(self, courseParams, noteParams):
        course_list = self.search_courses(courseParams);
        note_list = [];
        for course in course_list:
            listing = self.access_note.get_course_notes(course.id);
            for note in listing:
                note.course = course;
            note_list.extend(listing);
        note_list = search.filter_note_list(note_list, noteParams);
        return note_list;

