from ...logic.objects.user import User

class UsersAccessor:
    """ implementation of user accessor """

    def __init__(self, db_context):
        """
        constructor. 
        
        params:
            db_context - the database context
        """
        self.db_context = db_context
        self.db = db_context.db
        
        

    def get_user(self, id):
        """ 
        gets a user by its id.
        returns the user if it can be found or None if not.
        """
        user = None
        
        user_row = self.db(self.db.users.id == id).select().first()
        if (user_row != None):
            user = User( user_row.username,
                         user_row.role,
                         user_row.email,
                         user_row.password,
                         user_row.last_name,
                         user_row.first_name,
                         user_row.id)
        return user



    def insert_user(self, user):
        """
        inserts a user into the database
        """
        id = self.db.users.insert( username = user.username,
                                   email = user.email,
                                   password = user.password,
                                   last_name = user.last_name,
                                   first_name = user.first_name,
                                   role = user.role )
        return id



    def update_user(self, updated):
        """
        updates a user in the database
        args:
            updated - the user object that has been updated
        returns:
            True if the user was updated successfully
            False if not
        """
        result = self.db(self.db.users.id == updated.user_id).update( username = updated.username,
                                                                 email = updated.email,
                                                                 password = updated.password,
                                                                 last_name = updated.last_name,
                                                                 first_name = updated.first_name,
                                                                 role = updated.role )
        return result != None #TODO: Investigate this. I'm not sure what an update returns????



    def delete_user(self, id):
        """
        deletes a user in the database
        args:
            id - the id of the user to delete, or, a user object
        returns:
            True if the user was successfully deleted
            False if not
        """
        result = self.db(self.db.users.id == id).delete()
        
        return result != None #TODO: Investigate this. I'm not sure what a delete returns????



    def get_user_list(self):
        """
        Returns an array of all users in the database
        """
        temp_user_list = self.db(self.db.users.id >= 0).select().as_list()
        user_list = []
        for row in temp_user_list:
            user = User( row['username'],
                         row['role'],
                         row['email'],
                         row['password'],
                         row['last_name'],
                         row['first_name'],
                         row['id'] )
            user_list.append(user)
        
        return user_list
        
