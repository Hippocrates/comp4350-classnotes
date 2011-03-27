from ...logic.objects.enrollment import Enrollment

class EnrollmentsAccessorStub:
    """ stub implementation of enrollment accessor """

    def __init__(self):
        """
        constructor. 
        
        params:
            db_context - the database context
        """
        self.next_id = 5
        self.enrollment_list = [
                Enrollment(1, 1, 1),
                Enrollment(1, 2, 2),
                Enrollment(2, 1, 3),
                Enrollment(2, 2, 4)
        ]


    def insert_enrollment(self, enrollment):
        """
        inserts a enrollment into the database
        """
        id = self.next_id
        enrollment.enrollment_id = id 
        self.enrollment_list.append(enrollment)

        self.next_id = self.next_id + 1
        return id 
        
        
        
    def delete_enrollment(self, id):
        """
        deletes a enrollment in the database
        args:
            id - the id of the enrollment to delete, or, a enrollment object
        returns:
            True if the enrollment was successfully deleted
            False if not
        """
        if hasattr(id, 'enrollment_id'):
            id = id.enrollment_id

        for i, enrollment in enumerate(self.enrollment_list):
            if enrollment.enrollment_id == id:
                self.enrollment_list.remove(enrollment)
                return True
        return False

    
    
    def get_user_enrollments(self, user_id):
        """
        Returns an array of all enrollments in the database
        """
        return [e for e in self.enrollment_list if e.user_id == user_id]
        
