from ...logic.objects.enrollment import Enrollment

class EnrollmentAccess:
    """The following can be used to access enrollment functionality"""
    def __init__(self, access_enrollment):
        """ to initialize a user access instance"""
        self.access_enrollment = access_enrollment;
        
    def insert_enrollment(self, user_id, course_id):
        enrollment = Enrollment(user_id, course_id)
        result = False
        if self.access_enrollment.insert_enrollment(enrollment) != None:
            result = True
        return result
        
        
        
    def delete_enrollment(self, id):
        result = self.access_enrollment.delete_enrollment(id)
        
        return result != None #TODO: Investigate this. I'm not sure what a delete returns????

    
    
    def get_user_enrollments(self, user_id):
        enrollment_list = self.access_enrollment.get_user_enrollments(user_id)
        return enrollment_list