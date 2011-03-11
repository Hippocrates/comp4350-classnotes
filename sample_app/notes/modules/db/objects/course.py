class Course:
    FORMAT = "%(dept)s %(number)s %(section)s"
    """ this is a class which holds information about a course """
    def __init__(self, dept, number, section, instructor, id = None):
        """ Constructor for the course class

        Params: 
            dept - the department of the course, eg. COMP
            number - the number of the course, eg. 1010
            section - the section of the course, eg A01
            instructor - the instructor of the course
            id - the id of the course. Leave blank when creating a new note
        """
        self.dept = dept
        self.number = number
        self.section = section
        self.instructor = instructor
        self.id = id
    
    def __str__(self):
        """ tostring method of the course
        sample return: COMP 1010 A01
        """
        return Course.FORMAT % dict(dept=self.dept, number=self.number, section=self.section,
                                    instructor=self.instructor, id=self.id)


