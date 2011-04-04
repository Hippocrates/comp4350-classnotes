from ..objects.note import Note
from ..user_access.user_control import UserControl
from searcher import Searcher
from course_search_params import CourseSearchParams
from ..objects.user import User

from datetime import date, datetime

class SubmitNote:
    """The following can be used to submit a note"""
    def __init__(self, access_course, access_note, access_user, access_enrollment):
        """ to initialize a submit note instance """
        self.access_course = access_course;
        self.access_note = access_note;
        self.access_user = access_user;
        self.access_enrollment = access_enrollment;
        self.searcher = Searcher(self.access_course, self.access_note, self.access_user);
        self.userControl = userControl = UserControl(self.access_user, self.access_enrollment)

    """in later iterations we will add a userID, and a file directly fileID, for now they are the same as a note"""				 
    def submit_note(self, start_date, end_date, notes, user_id, department, number, section=None):
        possible_courses = self.searcher.search_courses(CourseSearchParams(department=department, number=number, section=section));

        user = self.access_user.get_user(user_id);
        
        if len(possible_courses) == 1 and (user.role == User.ROLE_ADMIN or (user.role == User.ROLE_SUBMITTER and self.userControl.is_user_enrolled(user_id, possible_courses[0].id) == True)):
		    notesUploadFile = self.access_note.store_notes_file(notes.file, notes.filename);
            
		    note = Note(start_date, end_date, notesUploadFile, possible_courses[0].id, user_id, datetime.now());
		    """with our note object created, submit to our db."""				 
		    """our note is submitted"""
		    return self.access_note.insert_note(note);
        else:
            # was not able to submit note
            return None;

    def update_note_file(self, note_id, user_id, notes):
        user = self.access_user.get_user(user_id);
        note = self.access_note.get_note(note_id);
        note.notes = self.access_note.store_notes_file(notes.file, notes.filename);
        note.modified_by = user_id;
        note.modified_on = datetime.now();
        return self.access_note.update_note(note);

    def remove_note(self, note_id):
        return self.access_note.delete_note(note_id);
