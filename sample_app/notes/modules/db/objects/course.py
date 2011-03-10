class Course:
    """ this is a class which holds information about a course """
    def __init__(self, id, name, instructor):
        """ Constructor for the course class

        Params: 
            id - the id of the course
            name - the name of the course
            instructor - the instructor of the course
        """
        self.id = id
        self.name = name
        self.instructor = instructor

