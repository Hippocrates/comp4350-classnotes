from ...db.access.notes import NotesAccessor
from ...db.access.courses import CoursesAccessor
from note import Note
from course import Course

class SearchNotes:
"""implementation of the search note instance"""

def make_access_note(self,database):
	return NoteAccessor(database)

def make_access_course(self,database):
	return CourseAccessor(database)

def __init__(self,database):
		""" to initialize a search note		"""
		self.notes = make_access_note(database)
		self.courses = make_access_course(database)
		
"""the following method assumes we are always given a department and course id, all other fields are not necessary (just put None in other parameters to not use them"""
def search_notes(self, department,courseNumber,section,targetDate,instructor):
        """
        returns an array of all notes in the database for course course.
        """
		totalList = self.notes.get_notes_list()
		"""we are going to begin eliminating elements of our list by applying each constraint (if there is no entry for an attribute, just ignore it)"""
		"""now we are going to augment with course objects corresponding to our note"""
		for nt in totalList:
			nt.course = self.courses.get_courses(nt.course_id)
		"""now we have all the data to search. IMPORTANT TO NOTE, to get the course instance use the course attribute"""
		totalList = nt for nt in totalList if(nt.course.dept == department && nt.course.number) 
		"""we have eliminated all courses which do not match our course id"""
		
		"""next check if there is a section"""
		if(section != None)
			totalList = nt for nt in totalList if(nt.course.section == section)
		
		"""now an instructor?"""
		if(instructor != None)
			totalList = nt for nt in totalList if(nt.course.instructor == instructor)
		
		"""check the target date (if we have one) but, it is really important we assume we were given correct ranges"""
		if(targetDate != None)
			totalList = nt for nt in totalList if(nt.created_on == targetDate)
		
		"""now we should have a reduced list totalList to return!"""
		
		
return totalList;

