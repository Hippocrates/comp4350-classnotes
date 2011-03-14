from datetime import date

def courses():
    # insert course1
    new_course1 = Course("ENTR", "2020", "A01", "Litz")
    new_course1_id = access_course.insert_course(new_course1)
    
    # get course1
    course_1 = access_course.get_course(new_course1_id)
    
    # update course1
    course_1.dept = "PSYC"
    access_course.update_course(course_1)
    
    # insert course2
    new_course2 = Course("COMP", "1010", "A01", "Bla")
    new_course2_id = access_course.insert_course(new_course2)
    
    # insert course3
    new_course3 = Course("COMP", "1020", "A01", "Mhm")
    new_course3_id = access_course.insert_course(new_course3)
    
    # delete course3
    access_course.delete_course(new_course3_id)

    # get the list of all courses
    course_list = access_course.get_course_list()

    # return hash for easy viewing
    return dict(course_list = ["%s" % course for course in course_list])


def notes():
    #insert note1
    new_note1 = Note(date.today(), date.today(), "testnote1.pdf", 1, 1)
    new_note1_id = access_note.insert_note(new_note1)
    
    #insert note2
    new_note2 = Note(date.today(), date.today(), "testnote2.pdf", 1, 1)
    new_note2_id = access_note.insert_note(new_note2)
    
    #insert note3
    new_note3 = Note(date.today(), date.today(), "testnote3.pdf", 1, 1)
    new_note3_id = access_note.insert_note(new_note3)
    
    # get note3
    note_3 = access_note.get_note(new_note3_id)
    
    # update note3
    note_3.notes = "Some_other_file.pdf"
    access_note.update_note(note_3)

    #delete note2
    access_note.delete_note(new_note2_id)


    # get the list of all nots
    note_list = access_note.get_note_list()

    # get the notes for course 1
    course_notes = access_note.get_course_notes(1)

    # return hash for easy viewing
    return dict(note_list = ["%s" % note for note in note_list],
                course_notes = ["%s" % note for note in course_notes])
