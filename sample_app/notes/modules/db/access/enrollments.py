from ...logic.objects.enrollment import Enrollment

class EnrollmentsAccessor:
    """ implementation of enrollment accessor """

    def __init__(self, db_context):
        """
        constructor. 
        
        params:
            db_context - the database context
        """
        self.db_context = db_context
        self.db = db_context.db



    def insert_enrollment(self, enrollment):
        """
        inserts a enrollment into the database
        """
        id = self.db.enrollments.insert( user_id = enrollment.user_id,
                                         course_id = enrollment.course_id )
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
        result = self.db(self.db.enrollments.id == id).delete()
        
        return result != None #TODO: Investigate this. I'm not sure what a delete returns????

    
    
    def get_user_enrollments(self, user_id):
        """
        Returns an array of all enrollments in the database
        """
        temp_enrollment_list = self.db(self.db.enrollments.user_id == user_id).select().as_list()
        enrollment_list = []
        for row in temp_enrollment_list:
            enrollment = Enrollment( row['id'],
                                     row['course_id'],
                                     row['id'] )
            enrollment_list.append(enrollment)
        
        return enrollment_list
