class Note:
    """ this is a class which holds information about a note entry """
    def __init__(self, id, start_date, end_date, notes, course, 
                 created_by, created_on, modified_by, modified_on):
        """ Constructor for note entry.
        Params: 
            id - id of the note
            start_date - start date of the notes
            end_date - end date of the notes
            notes - the file for the nots
            course - the course the notes are tied to
            created_by - the person who created the notes
            created_on - when the notes were created
            modified_by - who last modified the notes
            modified_on - when the notes were last modified
        """
        self.id = id
        self.start_date = start_date
        self.end_date = end_date
        self.notes = notes # the notes file
        self.course = course
        self.created_by = created_by
        self.created_on = created_on
        self.modified_by = modified_by
        self.modified_on = modified_on
