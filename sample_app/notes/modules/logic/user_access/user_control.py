from ..objects.user import User
from ..objects.enrollment import Enrollment

class UserControl:
    """The following can be used to check user access rights"""
    def __init__(self, access_user, access_enrollment, access_course):
        """ to initialize a user access instance"""
        self.access_user = access_user;
        self.access_enrollment = access_enrollment;
        self.access_course = access_course;

    def get_user(self, id):
        user = self.access_user.get_user(id)
        return user

    def create_user(self,username,role,email,password,last_name,first_name):
        id=self.access_user.insert_user(User(username, role, email, password, last_name, first_name))
        return id != None

    def update_user(self,user):
        result = None
        if(user != None):
            result = self.access_user.update_user(user)
        return result != None
    
    def delete_user(self, id):
        result = self.access_user.delete_user(id)
        return result != None
    
    def add_user_enrollment(self, user_id, course_id):
        if not self.is_user_enrolled(user_id, course_id):
            try:
                self.access_enrollment.insert_enrollment(Enrollment(user_id, course_id));
                return True;
            except e:
                return False;
        return False;
        
    def remove_user_enrollment(self, user_id, course_id):
        enrollment_list = self.access_enrollment.get_user_enrollments(user_id);
        for enrollment in enrollment_list:
            if enrollment.course_id == course_id:
                self.access_enrollment.delete_enrollment(enrollment.id);
                return True;
        return False;

    def is_user_enrolled(self, user_id, course_id):
        enrollment_list = self.access_enrollment.get_user_enrollments(user_id);
        for enrollment in enrollment_list:
            if enrollment.course_id == course_id:
                return True;
        return False;

    def get_user_courses(self, user_id):
        enrollment_list = self.access_enrollment.get_user_enrollments(user_id);
        course_list = [];
        for enrollment in enrollment_list:
            course_list.append(self.access_course.get_course(enrollment.course_id));
        return course_list;
		
		
