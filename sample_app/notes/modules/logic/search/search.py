import difflib;

def fuzzy_search(a, b):
    matcher = difflib.SequenceMatcher(None, a, b);
    return matcher.ratio() > 0.8;

def course_instructor_filter(course, instructorName):
    return fuzzy_search(course.instructor.upper(), instructorName.upper());

def course_dept_filter(course, deptCode):
    return course.dept.upper() == deptCode.upper();

def course_number_filter(course, number):
    return int(course.number) == int(number);

def course_section_filter(course, section):
    return course.section.upper() == section.upper();

def filter_course_list(courseList, searchParams):
    result = courseList;

    if searchParams.department != None and len(searchParams.department) > 0:
        result = filter(lambda course: course_dept_filter(course, searchParams.department), result);
    if searchParams.section != None and len(searchParams.section) > 0:
        result = filter(lambda course: course_section_filter(course, searchParams.section), result);
    if searchParams.number != None and len(searchParams.number) > 0:
        result = filter(lambda course: course_number_filter(course, searchParams.number), result);
    if searchParams.instructor != None and len(searchParams.instructor) > 0:
        result = filter(lambda course: course_instructor_filter(course, searchParams.instructor), result);
    
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
