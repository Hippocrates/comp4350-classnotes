from ...logic.objects.course import Course

class CoursesAccessor:
    """ implementation of course accessor """

    def __init__(self, database):
        """
        constructor
        """
        self.db = database



    def get_course(self, id):
        """ 
        gets a course by its id.
        returns the course if it can be found or None if not.
        """
        course = None
        
        course_row = self.db(self.db.courses.id == id).select().first()
        if (course_row != None):
            course = Course( course_row.department,
                             course_row.number,
                             course_row.section,
                             course_row.instructor,
                             course_row.id)
        return course



    def insert_course(self, course):
        """
        inserts a course into the database and returns its ID
        """
        id = self.db.courses.insert( department = course.dept,
                                     number = course.number,
                                     section = course.section,
                                     instructor = course.instructor)
        return id



    def update_course(self, updated):
        """
        updates a course in the database
        args:
            updated - the course object that has been updated
        returns:
            True if the course was updated successfully
            False if not
        """
        result = self.db(self.db.courses.id == updated.id).update( department = updated.dept,
                                                                   number = updated.number,
                                                                   section = updated.section,
                                                                   instructor = updated.instructor)
        return result != None #TODO: Investigate this. I'm not sure what an update returns????



    def delete_course(self, id):
        """
        deletes a course in the database
        args:
            id - the id of the course to delete, or, a course object
        returns:
            True if the course was successfully deleted
            False if not
        """
        result = self.db(self.db.courses.id == id).delete()
        
        return result != None #TODO: Investigate this. I'm not sure what a delete returns????
        
        

    def get_course_list(self):
        """
        Returns an array of all courses in the database
        Returns an empty list if no courses exist
        """
        temp_course_list = self.db(self.db.courses.id >= 0).select().as_list()
        course_list = []
        for row in temp_course_list:
            course = Course( row['department'],
                             row['number'],
                             row['section'],
                             row['instructor'],
                             row['id'])
            course_list.append(course)
        
        return course_list

