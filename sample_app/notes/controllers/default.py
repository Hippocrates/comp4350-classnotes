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
SubmitNote = local_import('logic/search/submit_note', rebuildImports).SubmitNote;
EditCourses = local_import('logic/search/edit_courses', rebuildImports).EditCourses;
User = local_import('logic/objects/user', rebuildImports).User;

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
    
    form = FORM( TABLE(
            TR("Department: ", INPUT(_type='text', _name='dept', requires=IS_NOT_EMPTY())),
            TR("Course Number: ", INPUT(_type='text', _name='number', requires=[IS_NOT_EMPTY(),IS_INT_IN_RANGE(0,None)])),
            TR("Section: ", INPUT(_type='text', _name='section')),
            TR("Instructor: ", INPUT(_type='text', _name='instructor')),
            TR(INPUT(_type='submit', _name='submit')))
    )
    
    if form.accepts(request.vars, session, formname='CourseForm', keepvalues=True):
      EditCourses(access_course).submit_course(form.vars.dept, form.vars.number, form.vars.section, form.vars.instructor);
    elif form.errors:
      response.flash = 'Required course information missing'; 
      
    if request.vars.delete:
      EditCourses(access_course).delete_course(request.vars.delete);
      
    courses = Searcher(access_course, access_note).search_courses(CourseSearchParams());
    
    return dict(courses=courses, form=form);

def add_notes():
        """
        demo of building a form from the database model
        and accepting values from it
        """
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
          noteId = SubmitNote(access_course,access_note).submit_note(form.vars.start_date, form.vars.end_date, form.vars.upload, 1, form.vars.dept, form.vars.number, form.vars.section);
          if noteId != None:
            response.flash = 'Added note with ID: ' + str(noteId); 
          else:
            response.flash = 'Failed to add note';
          #TODO: grab User ID, replace the 1 above
                                          
                                          
        return dict(form=form)

def search_notes():
    """
    Search page, uses a custom FORM object
    """
    form = FORM( TABLE(
        TR("Department ID: ", INPUT(_type='text', _name='dept', requires=IS_NOT_EMPTY())),
        TR("Course Number: ", INPUT(_type='text', _name='number', requires=IS_NOT_EMPTY())),
        TR("Section ID: ", INPUT(_type='text', _name='section')),
        TR("Instructor: ", INPUT(_type='text', _name='instructor')),
        TR(INPUT(_type='submit', _name='submit')))
    )

    searchResult = None;

    if form.accepts(request.vars, session, formname='SearchForm', keepvalues=True):
        courseParams = CourseSearchParams(form.vars.dept, form.vars.number, form.vars.section, form.vars.instructor);
        noteParams = NoteSearchParams();
        searchResult = Searcher(access_course,access_note).search_notes(courseParams, noteParams);
        
    elif form.errors:
        response.flash = 'At least the department code and the course number are required';
        
    return dict(form=form, results=searchResult);

def create_user():
    """
    Admin page to add a user to the system with a given role
    """
    roles = User.list_roles();
    
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
        response.flash = 'Successfully added user %s with role #%d' % (request.vars['username'], User.get_role_id(request.vars['role']))
    elif form.errors:
        response.flash = 'Some fields were not entered correctly'

    return dict(form=form)

def user_admin():
    """
    A control page for administrators
    """
    if len(request.args) == 1:
      userId = request.args[0];
    else:
      session.flash = T('invalid request');
      redirect(URL('index'));

    coursesForm = FORM( TABLE(
        TR("Department ID: ", INPUT(_type='text', _name='dept', requires=IS_NOT_EMPTY())),
        TR("Course Number: ", INPUT(_type='text', _name='number', requires=IS_NOT_EMPTY())),
        TR("Section ID: ", INPUT(_type='text', _name='section')),
        TR("Instructor: ", INPUT(_type='text', _name='instructor')),
        TR(INPUT(_type='submit', _name='submit')))
    )

    possibleCourses = None;
    userCourses = []; # this is where I would search for user's courses

    if coursesForm.accepts(request.vars, session, formname='CoursesForm', keepvalues=True):
        courseParams = CourseSearchParams(coursesForm.vars.dept, coursesForm.vars.number, coursesForm.vars.section, coursesForm.vars.instructor);
        searchResult = Searcher(access_course,access_note).search_courses(courseParams);
        if len(searchResult) == 0:
            response.flash = 'Could not find a course matching your description';
        elif len(searchResult) > 1:
            possibleCourses = searchResult;
        else:
            response.flash = 'Good enough...'
            # I can't decide whether it would be better to do this directly, or via a post...
    elif coursesForm.errors:
        response.flash = 'Error in your course request';

    if request.vars.remove_course != None:
        # remove a course from this user with the given id
        response.flash = 'removed course %s from user (assuming it was there in the first place)' % (request.vars.remove_course);

    if request.vars.insert_course != None:
        # same idea
        response.flash = 'inserted course %s to user (assuming it wasnt already there in the first place)' % (request.vars.insert_course);

    return dict(userCourses=userCourses,coursesForm=coursesForm,possibleCourses=possibleCourses);

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
