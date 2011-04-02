# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################

rebuildImports = True;

Searcher=local_import('logic/search/searcher', rebuildImports).Searcher;
CourseSearchParams=local_import('logic/search/course_search_params', rebuildImports).CourseSearchParams;
NoteSearchParams=local_import('logic/search/note_search_params', rebuildImports).NoteSearchParams;
UserSearchParams=local_import('logic/search/user_search_params', rebuildImports).UserSearchParams;
SubmitNote = local_import('logic/search/submit_note', rebuildImports).SubmitNote;
EditCourses = local_import('logic/search/edit_courses', rebuildImports).EditCourses;
User = local_import('logic/objects/user', rebuildImports).User;
UserControl = local_import('logic/user_access/user_control', rebuildImports).UserControl;

# global logic objects
editCourses = EditCourses(access_course);
searcher = Searcher(access_course, access_note, access_user);
submitNotes = SubmitNote(access_course,access_note,access_user,access_enrollment)
userControl = UserControl(access_user, access_enrollment);

def index():
    """
    sample controller

    controllers return a dictionary to the view

    in this case, just select all the notes and return them to the view
    """
    all_notes = db().select(db.notes.ALL, orderby=db.notes.end_date)
    all_courses = db().select(db.courses.ALL, orderby=db.courses.number)
    
    return dict(notes=all_notes, courses=all_courses)

def courses():
    """
    Controller for editing (add, remove, edit) courses
    """
    if authed_user == None or authed_user.role != User.ROLE_ADMIN:
        session.flash = T('You are not authorized to view that page');
        redirect(URL('index'));
    
    form = FORM( TABLE(
            TR("Department: ", INPUT(_type='text', _name='dept', requires=IS_NOT_EMPTY())),
            TR("Course Number: ", INPUT(_type='text', _name='number', requires=[IS_NOT_EMPTY(),IS_INT_IN_RANGE(0,None)])),
            TR("Section: ", INPUT(_type='text', _name='section', requires=IS_NOT_EMPTY())),
            TR("Instructor: ", INPUT(_type='text', _name='instructor', requires=IS_NOT_EMPTY())),
            TR(INPUT(_type='submit', _name='submit')))
    )
    
    if form.accepts(request.vars, session, formname='CourseForm', keepvalues=True):
        editCourses.submit_course(form.vars.dept, form.vars.number, form.vars.section, form.vars.instructor);
    elif form.errors:
        response.flash = 'Required course information missing'; 
      
    if request.vars.delete:
        deleteId = int(request.vars.delete)
        editCourses.delete_course(deleteId);
        session.flash = 'Course %d deleted' % (deleteId);
        redirect("courses");
      
    courses = searcher.search_courses(CourseSearchParams());
    
    return dict(courses=courses, form=form);

def add_notes():
    """
    demo of building a form from the database model
    and accepting values from it
    """
    if authed_user == None or (authed_user.role != User.ROLE_SUBMITTER and authed_user.role != User.ROLE_ADMIN):
        session.flash = T('You are not authorized to view that page');
        redirect(URL('index'));

    form = FORM( TABLE(
        TR("Department: ", INPUT(_type='text', _name='dept', requires=IS_NOT_EMPTY())),
        TR("Course Number: ", INPUT(_type='text', _name='number', requires=IS_NOT_EMPTY())),
        TR("Section: ", INPUT(_type='text', _name='section')),
        TR("Start Date: ", INPUT(_class='date', _type='date', _name='start_date', requires=[IS_NOT_EMPTY(),IS_DATE()])),
        TR("End Date: ", INPUT(_class='date', _type='date', _name='end_date', requires=[IS_NOT_EMPTY(),IS_DATE()])),
        TR("Notes file (.pdf only): ", INPUT(_type='file', _name='upload', requires=IS_UPLOAD_FILENAME(extension='pdf'))),
        TR(INPUT(_type='submit', _name='submit')))
    )

    if form.accepts(request.vars, session, formname='AddForm', keepvalues=True):
        noteId = submitNotes.submit_note(form.vars.start_date, form.vars.end_date, form.vars.upload, authed_user.user_id, form.vars.dept, form.vars.number, form.vars.section);
        if noteId != None:
            response.flash = 'Added note with ID: ' + str(noteId);
        else:
            response.flash = 'You are not authorized to submit notes for that course';
    elif form.errors:
        response.flash = 'Failed to add note';                  

    return dict(form=form)

def search_notes():
    """
    Search page, uses a custom FORM object
    """
    if authed_user == None:
      session.flash = T('You are not authorized to view that page');
      redirect(URL('index'));
      
    form = FORM( TABLE(
        TR("Department ID: ", INPUT(_type='text', _name='dept', requires=IS_NOT_EMPTY())),
        TR("Course Number: ", INPUT(_type='text', _name='number', requires=IS_NOT_EMPTY())),
        TR("Section ID: ", INPUT(_type='text', _name='section')),
        TR("Instructor: ", INPUT(_type='text', _name='instructor')),
        TR("Submitter Username: ", INPUT(_type='text', _name='username')),
        TR("Submitter First Name: ", INPUT(_type='text', _name='first_name')),
        TR("Submitter Last Name: ", INPUT(_type='text', _name='last_name')),
        TR(INPUT(_type='submit', _name='submit')))
    )

    searchResult = None;

    if form.accepts(request.vars, session, formname='SearchForm', keepvalues=True):
        courseParams = CourseSearchParams(form.vars.dept, form.vars.number, form.vars.section, form.vars.instructor);
        noteParams = NoteSearchParams();
        userParams = UserSearchParams(form.vars.username, form.vars.first_name, form.vars.last_name);
        searchResult = searcher.search_notes(courseParams, noteParams);
        searchResult = filter(lambda note: userControl.can_view_note(authed_user, note), searchResult);
    elif form.errors:
        response.flash = 'At least the department code and the course number are required';
        
    return dict(form=form, results=searchResult);

def create_user():
    """
    Admin page to add a user to the system with a given role
    """
    if authed_user == None or authed_user.role != User.ROLE_ADMIN:
        session.flash = T('You are not authorized to view that page');
        redirect(URL('index'));

    roleTable = {'Consumer':User.ROLE_CONSUMER, 'Submitter':User.ROLE_SUBMITTER, 'Administrator':User.ROLE_ADMIN}
    roles = roleTable.keys();
    
    form = FORM( TABLE(
        TR("Login Name: ", INPUT(_type='text', _name='username', requires=IS_NOT_EMPTY())), # possibly 'IS_SLUG()' as well
        TR("User Type: ", SELECT(*roles, _name='role', requires=IS_IN_SET(roles))),
        TR("Default Password: ", INPUT(_type='text', _name='password', requires=IS_NOT_EMPTY())),
        TR("Last Name: ", INPUT(_type='text', _name='last_name', requires=IS_NOT_EMPTY())),
        TR("First Name: ", INPUT(_type='text', _name='first_name', requires=IS_NOT_EMPTY())),
        TR("Email Address: ", INPUT(_type='text', _name='email', requires=IS_EMAIL())),
        TR(INPUT(_type='submit', _name='submit')))
    )

    if form.accepts(request.vars, session, formname='CreateForm', keepvalues=False):
        passWordHash,errors = CRYPT()(request.vars['password']);
        created = userControl.create_user(
            request.vars['username'],
            roleTable[request.vars['role']],
            request.vars['email'],
            passWordHash,
            request.vars['last_name'],
            request.vars['first_name']);
        if created != None:
            response.flash = 'Successfully added user %s' % (request.vars['username'])
            redirect(URL('user_admin/%d' % (created)));
        else:
            response.flash = 'Could not create user!';
    elif form.errors:
        response.flash = 'Some fields were not entered correctly'

    return dict(form=form)

def search_users():
    form = FORM( TABLE(
        TR("Login Name: ", INPUT(_type='text', _name='username', requires=IS_NOT_EMPTY())),
        TR("First Name: ", INPUT(_type='text', _name='first_name')),
        TR("Last Name: ", INPUT(_type='text', _name='last_name')),
        TR(INPUT(_type='submit', _name='submit'))
        )
    )

    possibleUsers = None;

    if form.accepts(request.vars, session, formname='SearchUserForm', keepvalues=True):
        userParams = UserSearchParams(form.vars.username, form.vars.first_name, form.vars.last_name);
        possibleUsers = searcher.search_users(userParams);
    elif form.errors:
        response.flash = 'Could not fulfil your request'

    return dict(form=form, possibleUsers=possibleUsers);

def user_info():
    if len(request.args) == 1:
        userId = int(request.args[0]);
        user = userControl.get_user(userId);
        if user == None:
            session.flash = T('User %d does not exist' % (userId));
            redirect(URL('index'));
    else:
        session.flash = T('invalid request');
        redirect(URL('index'));

    canAdminUser = authed_user.role == User.ROLE_ADMIN;

    return dict(user=user, canAdminUser=canAdminUser);

def user_admin():
    """
    A control page for administrators
    """
    if len(request.args) == 1:
        userId = int(request.args[0]);
        if userControl.get_user(userId) == None:
            session.flash = T('User %d does not exist' % (userId));
            redirect(URL('index'));
    else:
        session.flash = T('invalid request');
        redirect(URL('index'));

    if authed_user == None or authed_user.role != User.ROLE_ADMIN:
        session.flash = T('You are not authorized to view that page');
        redirect(URL('index'));

    coursesForm = FORM( TABLE(
        TR("Department ID: ", INPUT(_type='text', _name='dept', requires=IS_NOT_EMPTY())),
        TR("Course Number: ", INPUT(_type='text', _name='number', requires=IS_NOT_EMPTY())),
        TR("Section ID: ", INPUT(_type='text', _name='section')),
        TR("Instructor: ", INPUT(_type='text', _name='instructor')),
        TR(INPUT(_type='submit', _name='submit')))
    )

    possibleCourses = None;

    if coursesForm.accepts(request.vars, session, formname='CoursesForm', keepvalues=True):
        courseParams = CourseSearchParams(coursesForm.vars.dept, coursesForm.vars.number, coursesForm.vars.section, coursesForm.vars.instructor);
        searchResult = searcher.search_courses(courseParams);
        if len(searchResult) == 0:
            response.flash = 'Could not find a course matching your description';
        elif len(searchResult) > 1:
            possibleCourses = searchResult;
        else:
            request.vars.insert_course = searchResult[0].id;
    elif coursesForm.errors:
        response.flash = 'Error in your course request';

    deleteUserForm = FORM("Delete this user? ", INPUT(_type='submit', _name='submit'));

    if deleteUserForm.accepts(request.vars, session, formname="DeleteUserForm"):
        if userId == authed_user.user_id:
            response.flash = "You probably don't want to delete yourself"
        else:
            userControl.delete_user(userId);
            session.flash = 'User %d deleted' % (userId);
            redirect(URL('index'));
    elif deleteUserForm.errors:
        session.flash = 'Could not delete user %d' % (userId);

    if request.vars.remove_course != None:
        removed = userControl.remove_user_enrollment(userId, int(request.vars.remove_course));
        if removed:
            session.flash = 'removed course %s from user' % (request.vars.remove_course);
        else:
            session.flash = 'user was not enrolled in this course';
        redirect(URL('user_admin/%d' % (userId)))

    if request.vars.insert_course != None:
        added = userControl.add_user_enrollment(userId, int(request.vars.insert_course));
        if added:
            session.flash = 'added course %s to user' % (request.vars.insert_course);
        else:
            session.flash = 'user is already registered to this course';
        redirect(URL('user_admin/%d' % (userId)))

    userCourses = searcher.get_courses(userControl.get_user_courses(userId));

    return dict(userCourses=userCourses,coursesForm=coursesForm,deleteUserForm=deleteUserForm,possibleCourses=possibleCourses);

def note_info():
    """
    A control page to view information about notes
    """
    if len(request.args) == 1:
        noteId = int(request.args[0]);
        if searcher.get_note(noteId) == None:
            session.flash = T('Note %d does not exist' % (noteId));
            redirect(URL('index'));
    else:
        session.flash = T('invalid request');
        redirect(URL('index'));

    if not userControl.can_view_note(authed_user, noteId):
        session.flash = T('You are not authorized to view that page');
        redirect(URL('index'));

    canUserAdminNote = userControl.can_admin_note(authed_user, noteId);
    note = searcher.get_note(noteId);

    return dict(note=note, canUserAdminNote=canUserAdminNote);

    
def note_admin():
    """
    A control page to deal with note objects, currently a WIP
    """
    if len(request.args) == 1:
        noteId = int(request.args[0]);
        if searcher.get_note(noteId) == None:
            session.flash = T('Note %d does not exist' % (noteId));
            redirect(URL('index'));
    else:
        session.flash = T('invalid request');
        redirect(URL('index'));

    if not userControl.can_admin_note(authed_user, noteId):
        session.flash = T('You are not authorized to view that page');
        redirect(URL('index'));

    deleteNoteForm = FORM("Remove these notes? ", INPUT(_type='submit', _name='submit'));

    if deleteNoteForm.accepts(request.vars, session, formname="DeleteNoteForm"):
        submitNotes.remove_note(noteId);
        session.flash = 'Note %d deleted' % (noteId);
        redirect(URL('index'));
    elif deleteNoteForm.errors:
        session.flash = 'Could not delete note %d' % (userId);
        
    note = searcher.get_note(noteId);
    return dict(note=note, deleteNoteForm=deleteNoteForm);


def loremipsum():
    """ dummy page """
    return dict();
   

# these are default controllers enabled by web2py:

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request,db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    session.forget()
    return service()
