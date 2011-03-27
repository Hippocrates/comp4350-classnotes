from ...logic.objects.user import User

class UsersAccessorStub:
    """ stub implementation of user accessor """
        
    def __init__(self):
        """
        constructor for stub accessor
        """
        self.next_id =  5
        self.user_list = [
                User('sbutts', User.ROLE_CONSUMER, 'seymour@gmail.com', 'hash', 'Butts', 'Seymour', 1),
                User('ipfreely', User.ROLE_ADMIN, 'flowmaster@gmail.com', 'hash', 'Freely', 'I.P.', 2),
                User('theoc', User.ROLE_SUBMITTER, 'oliverc@gmail.com', 'hash', 'Clothesoff', 'Oliver', 3),
                User('mrotch', User.ROLE_ADMIN, 'mike.rotch@gmail.com', 'hash', 'Rotch', 'Mike', 4),
        ]


    def get_user(self, id):
        """ 
        gets a user by its id.
        returns the user if it can be found or None if not.
        """
        for user in self.user_list:
            if user.user_id == id:
                return user
        return None



    def insert_user(self, user):
        """
        inserts a user into the database
        """
        id = self.next_id
        user.user_id = id 
        self.user_list.append(user)

        self.next_id = self.next_id + 1
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
        for i, user in enumerate(self.user_list):
            if user.user_id == updated.user_id:
                self.user_list[i] == updated
                return True
        return False


    def delete_user(self, id):
        """
        deletes a user in the database
        args:
            id - the id of the user to delete, or, a user object
        returns:
            True if the user was successfully deleted
            False if not
        """
        if hasattr(id, 'user_id'):
            id = id.user_id

        for i, user in enumerate(self.user_list):
            if user.user_id == id:
                self.user_list.remove(user)
                return True
        return False



    def get_user_list(self):
        """
        Returns an array of all users in the database
        """
        return self.user_list
        
