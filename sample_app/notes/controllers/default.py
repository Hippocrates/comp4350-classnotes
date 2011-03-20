# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################

Searcher=local_import('logic/search/searcher').Searcher;
CourseSearchParams=local_import('logic/search/course_search_params').CourseSearchParams;
NoteSearchParams=local_import('logic/search/note_search_params').NoteSearchParams;
SubmitNote = local_import('logic/search/submit_note').SubmitNote;

def index():
    """
    sample controller

    controllers return a dictionary to the view

    in this case, just select all the notes and return them to the view
    """
    all_notes = db().select(db.notes.ALL, orderby=db.notes.end_date)
    return dict(notes=all_notes)

def add_notes():
        """
        demo of building a form from the database model
        and accepting values from it
        """
        """
        def notes_added(form):
                session.flash = "You successfully added some notes"
                redirect(URL('index'))
        form = crud.create(db.notes, onaccept=notes_added);
        """
        form = FORM(
            "Department: ", INPUT(_type='text', _name='dept', requires=IS_NOT_EMPTY()), BR(),
            "Course Number: ", INPUT(_type='text', _name='number', requires=IS_NOT_EMPTY()), BR(),
            "Section: ", INPUT(_type='text', _name='section', requires=IS_NOT_EMPTY()), BR(),
            "Start Date: ", INPUT(_type='date', _name='start_date', requires=[IS_NOT_EMPTY(),IS_DATE()]), BR(),
            "End Date: ", INPUT(_type='date', _name='end_date', requires=[IS_NOT_EMPTY(),IS_DATE()]), BR(),
            "Notes file (.pdf only): ", INPUT(_type='file', _name='upload', requires=IS_NOT_EMPTY()), BR(),
            INPUT(_type='submit', _name='submit')
        )
        
        noteId = None;
        
        if form.accepts(request.vars, session, formname='AddForm', keepvalues=True):
          noteId = SubmitNote(access_course,access_note).submit_note(form['start_date'], form['end_date'], form['upload'], 1, form['dept'], form['number'], form['section']);
          #TODO: grab User ID, replace the 1 above
                                          
                                          
        return dict(form=form, noteId = noteId)

def search_notes():
    """
    Search page, uses a custom FORM object
    """
    form = FORM(
        "Department ID: ", INPUT(_type='text', _name='dept', requires=IS_NOT_EMPTY()), BR(),
        "Course Number: ", INPUT(_type='text', _name='number', requires=IS_NOT_EMPTY()), BR(),
        "Section ID: ", INPUT(_type='text', _name='section'), BR(),
        "Instructor: ", INPUT(_type='text', _name='instructor'), BR(),
                INPUT(_type='submit', _name='submit')
    )

    searchResult = None;
    
    if form.accepts(request.vars, session, formname='SearchForm', keepvalues=True):
        # currently we are latched on logic giving us the ability
        # to actually query data, so I'm just pushing stub data out for now
        courseParams = CourseSearchParams(form['dept'], form['number'], form['section'], form['instructor']);
        noteParams = NoteSearchParams();
        searchResult = Searcher(access_course,access_note).search_notes(courseParams, noteParams);
        
    elif form.errors:
        response.flash = 'At least the department code and the course number are required';
        
    return dict(form=form, results=searchResult);

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
