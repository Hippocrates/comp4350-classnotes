
class User:
    """ this is a class which holds information about a user entry """
    ROLE_CONSUMER = 0
    ROLE_SUBMITTER = 1
    ROLE_ADMIN = 2
    MIN_ROLE = 0
    MAX_ROLE = 2
    def __init__(self, username, role, email, password_hash, lastName, firstName, user_id=None):
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
        if role < self.MIN_ROLE or role > self.MAX_ROLE:
             raise "Invalid role %d" % (role);
        self.role = role;

    def __str__(self):
        """ to string for user entry """
        return "User [user_id=%s, email=%s, lastName=%s, firstName=%s]" % \
                    (self.user_id, self.email, self.lastName, self.firstName)

    @staticmethod
    def list_roles():
        # return a copy of the list to avoid issues with non-immutability
        return list(_roles);

    def get_role_name(roleId):
        return _roles[roleId];

    @staticmethod
    def get_role_id(name):
        if name in _roles:
          return _roles.index(name)
        else:
          return None;
