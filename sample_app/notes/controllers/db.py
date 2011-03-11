from datetime import date

def courses():
    # get a single course
    course_1 = access_course.get_course(1)

    # update a single course
    course_1.dept = "PSYC"
    access_course.update_course(course_1)

    # delete a course
    access_course.delete_course(2)

    # insert a course
    new_course = Course("ENTR", "2020", "A01", "Litz")
    access_course.insert_course(new_course)

    # get the list of all courses
    course_list = access_course.get_course_list()


    # return hash for easy viewing
    return dict(course_1 = "%s" % course_1, course_list = ["%s" % course for course in course_list])


def notes():
    # get a note by id
    note_1 = access_note.get_note(1)
    
    # update a note
    note_1.notes = "Some other file.pdf"
    access_note.update_note(note_1)


    #delete a note
    access_note.delete_note(2)
    

    #insert a note
    new_note = Note(date.today(), date.today(), "testnote.pdf", 1, 1)
    access_note.insert_note(new_note)


    # get the list of all nots
    note_list = access_note.get_note_list()

    # get the notes for course 1
    course_notes = access_note.get_course_notes(1)

    # return hash for easy viewing
    return dict(note_1 = "%s" % note_1, note_list = ["%s" % note for note in note_list],
                        course_notes = ["%s" % note for note in course_notes])
