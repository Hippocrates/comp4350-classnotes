from ..objects.note import Note
from ..user_access.user_rights import UserRights
from searcher import Searcher
from course_search_params import CourseSearchParams

from datetime import date, datetime

class SubmitNote:
    """The following can be used to submit a note"""
    def __init__(self, access_course, access_note, access_user, access_enrollment):
        """ to initialize a submit note instance """
        self.access_course = access_course;
        self.access_note = access_note;
        self.access_user = access_user;
        self.access_enrollment = access_enrollment;
        self.searcher = Searcher(self.access_course, self.access_note);

    """in later iterations we will add a userID, and a file directly fileID, for now they are the same as a note"""				 
    def submit_note(self, start_date, end_date, notes, user_id, department, number, section=None):
        possible_courses = self.searcher.search_courses(CourseSearchParams(department=department, number=number, section=section));

        # eventually, this should cross-check with the courses the given user is allowed to submit for

        if len(possible_courses) == 1 and UserRights(self.access_user, self.access_enrollment).check_access_rights(user_id, possible_courses[0].id) == True:
		    notesUploadFile = self.access_note.store_notes_file(notes.file, notes.filename);
            
		    note = Note(start_date, end_date, notesUploadFile, possible_courses[0].id, user_id, datetime.now());
		    """with our note object created, submit to our db."""				 
		    """our note is submitted"""
		    return self.access_note.insert_note(note);
        else:
            # was not able to submit note
            return None;
