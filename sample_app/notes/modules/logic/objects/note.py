from datetime import datetime

class Note:
    """ this is a class which holds information about a note entry """
    def __init__(self, start_date, end_date, notes, course_id, 
                 created_by, created_on=None, modified_by=None, 
                 modified_on=None, id = None):
        """ Constructor for note entry.
        Params: 
            start_date - start date of the notes
            end_date - end date of the notes
            notes - the file for the nots
            course_id - the id of the course the notes are tied to
            created_by - the person who created the notes
            created_on - when the notes were created (default now)
            modified_by - who last modified the notes (default created_by)
            modified_on - when the notes were last modified
            id - id of the note, leave blank when creating a new note
        """
        self.start_date = start_date
        self.end_date = end_date
        self.notes = notes # the notes file
        self.course_id = course_id
        self.created_by = created_by
        self.created_on = created_on or datetime.now()
        self.modified_by = modified_by or created_by
        self.modified_on = modified_on or self.created_on
        self.id = id

    def __str__(self):
        """ to string for note entry """
        return "Note [ID=%s, Start=%s, End=%s, Notes=%s, Course=%s, Author=%s]" % \
                    (self.id, self.start_date, self.end_date, self.notes, self.course_id, self.created_by)
