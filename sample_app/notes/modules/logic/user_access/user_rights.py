from ..objects.user import User
from ..objects.enrollment import Enrollment

class UserRights:
    """The following can be used to check user access rights"""
    def __init__(self, access_user, access_enrollment):
        """ to initialize a user access instance"""
        self.access_user = access_user;
        self.access_enrollment = access_enrollment;
		
		
    def check_access_rights(self, user_id, course_id):
        result = False;
        if self.access_user.get_user(user_id).role == User.ROLE_SUBMITTER:
            enrollment_list = self.access_enrollment.get_user_enrollments(user_id);
            for enrollment in enrollment_list:
                if enrollment.course_id == course_id:
                    result = True;
		
        return result;
		
		