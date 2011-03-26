# when true db code is recompiled at each page load
# in production set to false and it will only be compiled once
db_debug_mode = True

Note = local_import('logic/objects/note', db_debug_mode).Note
Course = local_import('logic/objects/course', db_debug_mode).Course
User = local_import('logic/objects/user', db_debug_mode).User
Enrollment = local_import('logic/objects/enrollment', db_debug_mode).Enrollment

CoursesAccessor = local_import('db/access/courses', db_debug_mode).CoursesAccessor
NotesAccessor = local_import('db/access/notes', db_debug_mode).NotesAccessor
UsersAccessor = local_import('db/access/users', db_debug_mode).UsersAccessor
EnrollmentsAccessor = local_import('db/access/enrollments', db_debug_mode).EnrollmentsAccessor

access_course = CoursesAccessor(db_context)
access_note = NotesAccessor(db_context)
access_user = UsersAccessor(db_context)
access_enrollment = EnrollmentsAccessor(db_context)

authed_user = None
if auth.is_logged_in():
    user_id = auth.user.id
    authed_user = access_user.get_user(user_id)
