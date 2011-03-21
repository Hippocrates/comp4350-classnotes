from gluon.sql import Field
from gluon.validators import *

from ...logic.objects.note import Note
from datetime import date

class NotesAccessor:
    """ implementation of note accessor """

    def __init__(self, db_context):
        """
        constructor. 
        
        params:
            db_context - the database context
        """
        self.db_context = db_context
        self.db = db_context.db
        


    def get_note(self, id):
        """ 
        gets a note by its id.
        returns the note if it can be found or None if not.
        """
        note = None
        
        note_row = self.db(self.db.notes.id == id).select().first()
        if (note_row != None):
            note = Note( note_row.start_date,
                         note_row.end_date,
                         note_row.notes,
                         note_row.course_id,
                         note_row.created_by,
                         note_row.created_on,
                         note_row.modified_by,
                         note_row.modified_on,
                         note_row.id )
        return note



    def insert_note(self, note):
        """
        inserts a note into the database
        """
        id = self.db.notes.insert( start_date = note.start_date,
                                   end_date = note.end_date,
                                   notes = note.notes,
                                   course_id = note.course_id,
                                   created_by = note.created_by,
                                   created_on = note.created_on,
                                   modified_by = note.modified_by,
                                   modified_on = note.modified_on )
        return id



    def update_note(self, updated):
        """
        updates a note in the database
        args:
            updated - the note object that has been updated
        returns:
            True if the note was updated successfully
            False if not
        """
        result = self.db(self.db.notes.id == updated.id).update( start_date = updated.start_date,
                                                                 end_date = updated.end_date,
                                                                 notes = updated.notes,
                                                                 course_id = updated.course_id,
                                                                 created_by = updated.created_by,
                                                                 created_on = updated.created_on,
                                                                 modified_by = updated.modified_by,
                                                                 modified_on = updated.modified_on )
        return result != None #TODO: Investigate this. I'm not sure what an update returns????



    def delete_note(self, id):
        """
        deletes a note in the database
        args:
            id - the id of the note to delete, or, a note object
        returns:
            True if the note was successfully deleted
            False if not
        """
        result = self.db(self.db.notes.id == id).delete()
        
        return result != None #TODO: Investigate this. I'm not sure what a delete returns????



    def get_note_list(self):
        """
        Returns an array of all notes in the database
        """
        temp_note_list = self.db(self.db.notes.id >= 0).select().as_list()
        note_list = []
        for row in temp_note_list:
            note = Note( row['start_date'],
                         row['end_date'],
                         row['notes'],
                         row['course_id'],
                         row['created_by'],
                         row['created_on'],
                         row['modified_by'],
                         row['modified_on'],
                         row['id'])
            note_list.append(note)
        
        return note_list



    def get_course_notes(self, course_id):
        """
        returns an array of all notes in the database for course course 
        returns an empty list if no notes exist for the course
        """
        note_list = []
        rows = self.db(self.db.notes.course_id == course_id).select(self.db.notes.ALL)
        for row in rows:
            note_list.append( Note( row['start_date'],
                                    row['end_date'],
                                    row['notes'],
                                    row['course_id'],
                                    row['created_by'],
                                    row['created_on'],
                                    row['modified_by'],
                                    row['modified_on'],
                                    row['id']))
        
        return note_list
