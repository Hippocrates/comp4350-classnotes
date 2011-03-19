from ...db.access.notes import NotesAccessor
from ..objects.note import Note
from searcher import Searcher
from course_search_params import CourseSearchParams

from datetime import date, datetime

class SubmitNote:
    """The following can be used to submit a note"""
    def __init__(self, access_course, access_note):
        """ to initialize a submit note instance """
        self.access_course = access_course;
        self.access_note = access_note;
        self.searcher = Searcher(self.access_course, self.access_note);

    """in later iterations we will add a userID, and a file directly fileID, for now they are the same as a note"""				 
    def submit_note(self, start_date, end_date, notes, user_id, department, number, section=None):
        possible_courses = self.searcher.search_courses(CourseSearchParams(department=department, number=number, section=section));

        # eventually, this should cross-check with the courses the given user is allowed to submit for

        if len(possible_courses) == 1:
            note = Note(start_date, end_date, notes, possible_courses[0], user_id, datetime.now());
            """with our note object created, submit to our db."""				 
            """our note is submitted"""
            return self.access_note.insert_note(note);
        else:
            # was not able to submit note
            return None;
