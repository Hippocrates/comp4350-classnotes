
class User:
    """ this is a class which holds information about a user entry """
    ROLE_CONSUMER = 0
    ROLE_SUBMITTER = 1
    ROLE_ADMIN = 2
    MIN_ROLE = 0
    MAX_ROLE = 2
    def __init__(self, username, role, email, password, lastName, firstName, user_id=None):
        """ Constructor for user entry.
        Params: 
            username - the user's name
            email - the e-mail of the user
            password - the password of the user
            lastName - the last name of the user
            firstName - the first name of the user
            user_id - the id of the user
        """
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.last_name = lastName
        self.first_name = firstName
        if role < self.MIN_ROLE or role > self.MAX_ROLE:
             raise Exception("Invalid role %s" % str(role))
        self.role = role;

    def __str__(self):
        """ to string for user entry """
        return "User [user_id=%s, email=%s, lastName=%s, firstName=%s]" % \
                    (self.user_id, self.email, self.last_name, self.first_name)
