import difflib;

def fuzzy_search(a, b):
    matcher = difflib.SequenceMatcher(None, a, b);
    return matcher.ratio() > 0.8;

def course_instructor_filter(course, instructorName):
    return fuzzy_search(course.instructor, instructorName);

def course_dept_filter(course, deptCode):
    return course.dept == deptCode;

def course_number_filter(course, number):
    return course.number == number;

def course_section_filter(course, section):
    return course.section == section;

def filter_course_list(courseList, searchParams):
    result = courseList;
    
    if searchParams.instructor != None:
        result = filter(lambda course: course_instructor_filter(course, searchParams.instructor), result);
    if searchParams.department != None:
        result = filter(lambda course: course_dept_filter(course, searchParams.department), result);
    if searchParams.section != None:
        result = filter(lambda course: course_section_filter(course, searchParams.section), result);
    if searchParams.number != None:
        result = filter(lambda course: course_number_filter(course, searchParams.number), result);
        
    return result;

def note_course_filter(note, courseIds):
    return note.course_id in courseIds;

def note_user_filter(note, userIds):
    return note.created_by in userIds;

def note_created_after_filter(note, submissionDateTime):
    return note.created_on >= submissionDateTime;

def note_created_before_filter(note, submissionDateTime):
    return note.created_on <= submissionDateTime;

def note_range_filter(note, targetTime):
    return note.start_date <= targetTime and note.end_date >= targetTime;

def filter_note_list(noteList, noteSearchParams):
    result = noteList;

    if noteSearchParams.submittedAfter != None:
        result = filter(lambda note: note_created_after_filter(note, noteSearchParams.submittedAfter), result);
    if noteSearchParams.submittedBefore != None:
        result = filter(lambda note: note_created_before_filter(note, noteSearchParams.submittedBefore), result);
    if noteSearchParams.targetDate != None:
        result = filter(lambda note: note_range_filter(note, noteSearchParams.targetDate), result);
    
    return result;
