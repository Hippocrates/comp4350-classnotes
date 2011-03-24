class Enrolled:
    """ this is a class which holds information about a user entry """
    def __init__(self, user_id, course_id, enrolled_id=None):
        """ Constructor for user entry.
        Params: 
            user_id - user id
            course_id - course id
			enrolled_id - the id of that entry in the database
        """
        self.enrolled_id = enrolled_id
        self.user_id = user_id
        self.course_id = course_id
	
    def __str__(self):
        """ to string for enrolled entry """
        return "Enrolled [enrolled_id=%s, user_id=%s, course_id=%s]" % \
                    (self.enrolled_id, self.user_id, self.course_id)
