from .. objects.note import Note
from datetime import date

class AccessNoteStub:
    """ Stub implementation of note accessor """

    def make_note_stub(self, id, start_date, course_id, user_id):
        end_date = start_date.replace(day = start_date.day+2)
        filename = "Notes%d.%d.%d.C%d.pdf" % (start_date.year, start_date.month, start_date.day, course_id)
        return Note(start_date, end_date, filename, course_id, user_id, id=id)

    def __init__(self):
        """
        constructor for stub accessor
        """
        self._next_id = 4
        self.note_list = [
                self.make_note_stub(1, date(2011, 01, 01), 1, 1),
                self.make_note_stub(2, date(2011, 01, 01), 2, 1),
                self.make_note_stub(3, date(2011, 01, 01), 3, 1)
        ]

    def get_note(self, id):
        """ 
        gets a note by its id.
        returns the note if it can be found or None if not.
        """
        for note in self.note_list:
            if note.id == id:
                return note
        return None

    def insert_note(self, note):
        """
        inserts a note into the database
        """
        id = self._next_id
        note.id = id 
        self.note_list.append(note)

        self._next_id = self._next_id + 1
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
        for i, note in enumerate(self.note_list):
            if note.id == updated.id:
                self.note_list[i] == updated
                return True
        return False


    def delete_note(self, id):
        """
        deletes a note in the database
        args:
            id - the id of the note to delete, or, a note object
        returns:
            True if the note was successfully deleted
            False if not
        """
        if hasattr(id, 'id'):
            id = id.id

        for i, note in enumerate(self.note_list):
            if note.id == id:
                self.note_list.remove(note)
                return True
        return False

    def get_note_list(self):
        """
        Returns an array of all notes in the database
        """
        return self.note_list

    def get_course_notes(self, id):
        """
        returns an array of all notes in the database for course course 
        """
        return [note for note in self.note_list if note.course_id == id]
