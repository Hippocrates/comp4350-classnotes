from ...logic.objects.course import Course

class AccessCourseStub:
    """ Stub implementation of course accessor """

    def __init__(self):
        """
        constructor for stub accessor
        """
        self.next_id =  7
        self.course_list = [
                Course('COMP', '1010', 'A01', 'Penner', 1),
                Course('COMP', '1020', 'A01', 'Braico', 2),
                Course('COMP', '2160', 'A01', 'Zapp', 3),
                Course('COMP', '2140', 'A01', 'Mike Dom', 4),
                Course('COMP', '2150', 'A01', 'Anderson', 5),
                Course('MATH', '1500', 'A01', 'Gerhardt', 6)
        ]

    def get_course(self, id):
        """ 
        gets a course by its id.
        returns the course if it can be found or None if not.
        """
        for course in self.course_list:
            if course.id == id:
                return course
        return None

    def insert_course(self, course):
        """
        inserts a course into the database
        """
        id = self.next_id
        course.id = id 
        self.course_list.append(course)

        self.next_id = self.next_id + 1
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
        for i, course in enumerate(self.course_list):
            if course.id == updated.id:
                self.course_list[i] == updated
                return True
        return False


    def delete_course(self, id):
        """
        deletes a course in the database
        args:
            id - the id of the course to delete, or, a course object
        returns:
            True if the course was successfully deleted
            False if not
        """
        if hasattr(id, 'id'):
            id = id.id

        for i, course in enumerate(self.course_list):
            if course.id == id:
                self.course_list.remove(course)
                return True
        return False

    def get_course_list(self):
        """
        Returns an array of all courses in the database
        """
        return self.course_list

