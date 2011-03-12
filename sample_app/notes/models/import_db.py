# when true db code is recompiled at each page load
# in production set to false and it will only be compiled once
db_debug_mode = True


AccessCourseStub = local_import('db/access/course_stub', db_debug_mode).AccessCourseStub
AccessNoteStub = local_import('db/access/note_stub', db_debug_mode).AccessNoteStub


# will replace these with similar methods that persist to a database soon
access_course = AccessCourseStub()
access_note = AccessNoteStub()
