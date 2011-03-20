from ..objects.course import Course

class EditCourses:
    """The following can be used to edit courses. May want to move (along with submit_note?) to a different directory"""
    def __init__(self, access_course):
        """ to initialize an edit courses instance """
        self.access_course = access_course;

    """in later iterations, need to verify user has permission to edit courses"""				 
    def submit_course(self, dept, number, section, instructor, id = None):
      
        course = Course(dept, number, section, instructor, id);
        return self.access_course.insert_course(course);
    
    """delete a course; again, need to check permissions"""
    def delete_course(self, id):
        return self.access_course.delete_course(id);