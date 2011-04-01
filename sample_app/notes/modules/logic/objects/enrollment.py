class Enrollment:
    """ this is a class which holds information about an enrollments entry """
    def __init__(self, user_id, course_id, id=None):
        """ Constructor for user entry.
        Params: 
            user_id - user id
            course_id - course id
			enrollment_id - the id of that entry in the database
        """
        self.id = id
        self.user_id = user_id
        self.course_id = course_id
	
    def __str__(self):
        """ to string for enrolled entry """
        return "Enrolled [id=%s, user_id=%s, course_id=%s]" % \
                    (self.id, self.user_id, self.course_id)
