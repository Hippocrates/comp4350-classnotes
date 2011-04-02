from ..objects.note import Note
from ..objects.course import Course
import search;

class Searcher:
    def __init__(self, access_course, access_note, access_user):
        self.access_note = access_note;
        self.access_course = access_course;
        self.access_user = access_user;

    def search_courses(self, courseParams):
        course_list = self.access_course.get_course_list();
        return search.filter_course_list(course_list, courseParams);

    def search_users(self, userParams):
        user_list = self.access_user.get_user_list();
        return search.filter_user_list(user_list, userParams);
		
    def search_notes(self, courseParams, noteParams, userParams=None):
        course_list = self.search_courses(courseParams);
        
        note_list = [];
        for course in course_list:
            listing = self.access_note.get_course_notes(course.id);
            for note in listing:
                note.course = course;
            note_list.extend(listing);

        if userParams != None:
            user_list = self.search_users(userParams);
            if noteParams.targetUsers == None:
                noteParams.targetUsers = user_list;
            else:
                noteParams.targetUsers.extend(user_list);

        note_list = search.filter_note_list(note_list, noteParams);

        for note in note_list:
            note.submitter = self.access_user.get_user(note.created_by);
            
        return note_list;

    def get_note(self, id):
        note = self.access_note.get_note(id);
        if note != None:
            note.course = self.access_course.get_course(note.course_id);
        return note;

    def get_course(self, id):
        return self.access_course.get_course(id);

    def get_courses(self, id_list):
        print (str(id_list));
        return map(lambda id: self.get_course(id), id_list);
