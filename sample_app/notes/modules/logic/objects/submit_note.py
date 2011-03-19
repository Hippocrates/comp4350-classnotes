from ...db.access.notes import NotesAccessor
from note import Note

class SubmitNote:
"""The following can be used to submit a note"""

def make_access_note(self,database):
	return NoteAccessor(database)

def make_access_course(self,database):
	return CourseAccessor(database)

def __init__(self,database):
		""" to initialize a submit note instance """
		self.notes = make_access_note(database)
		self.courses = make_access_course(database)

"""just to abstract the creation of a note."""
def create_note(self, start_date, end_date, notes, course_id, 
                 created_by, created_on=None, modified_by=None, 
                 modified_on=None, id = None)
	return Note(start_date, end_date, notes, course_id,
	             created_by, created_on=None, modified_by=None, 
                 modified_on=None, id = None)

"""in later iterations we will add a userID, and a file directly fileID, for now they are the same as a note"""				 
def submit_note(self, start_date, end_date, notes, course_id, 
                 created_by, created_on=None, modified_by=None, 
                 modified_on=None, id = None):
     note = create_note(start_date, end_date, notes, course_id, 
                 created_by, created_on=None, modified_by=None, 
                 modified_on=None, id = None);
"""with our note object created, submit to our db."""				 
	 self.notes.insert_note(note);
"""our note is submitted"""
