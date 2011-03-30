from ..objects.user import User

class UsersAccess:
    """The following can be used to access user functionality"""
    def __init__(self, access_user):
        """ to initialize a user access instance"""
        self.access_user = access_user;
        
    def get_user(self, id):
        user = None
        user = self.access_user.get_user(id)
        return user



    def insert_user(self,username,role,email,password,last_name,first_name):
        user = None
        user = User(username, role, email, password, last_name, first_name)
        if(user != None):
            id=self.access_user.insert_user(user)
        return id




    def update_user(self,user):
        result = None
        if(user != None):
            result = self.access_user.update_user(user)
        return result != None #TODO: Investigate this. I'm not sure what an update returns????



    def delete_user(self, id):
        result = self.access_user.delete_user(id)
        
        return result != None #TODO: Investigate this. I'm not sure what a delete returns????



    def get_user_list(self):
        user_list = self.access_user.get_user_list()
        
        return user_list	
		