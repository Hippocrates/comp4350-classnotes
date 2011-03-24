from ...logic.objects.enrolled import Enrolled

class EnrollmentsAccessor:
    """ implementation of enrollment accessor """

    def __init__(self, db_context):
        """
        constructor. 
        
        params:
            db_context - the database context
        """
        self.db_context = db_context
        self.db = db_context.db
