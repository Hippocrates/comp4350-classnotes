# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################

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
        def notes_added(form):
                session.flash = "You successfully added some notes"
                redirect(URL('index'))
        form = crud.create(db.notes, onaccept=notes_added)
        return dict(form=form)

def search_notes():
    """
    A (very) basic idea of how the search page might look.
    Uses a custom FORM object
    """
    form = SQLFORM.factory(
        Field('Course_ID', requires=IS_NOT_EMPTY()))
    
    searchResult = None
    if form.accepts(request.vars, session, keepvalues=True):
        searchResult = 'Here is where I would output the search results'
    elif form.errors:
        response.flash = 'Search field cannot be empty, because I said so'
    return dict(form=form, results=searchResult);


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
