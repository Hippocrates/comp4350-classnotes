from datetime import datetime

class User:
    """ this is a class which holds information about a user entry """
    def __init__(self, username, email, password_hash, lastName, firstName, user_id=None):
        """ Constructor for user entry.
        Params: 
            username - the user's name
            email - the e-mail of the user
			password_hash - the password of the user
			lastName - the last name of the user
			firstName - the first name of the user
			user_id - the id of the user
        """
        self.user_id = user_id
        self.username = username
        self.email = email
		self.password_hash = password_hash
        self.lastName = lastName
		self.firstName = firstName
	
    def __str__(self):
        """ to string for user entry """
        return "User [user_id=%s, email=%s, lastName=%s, firstName=%s]" % \
                    (self.user_id, self.email, self.lastName, self.firstName)
