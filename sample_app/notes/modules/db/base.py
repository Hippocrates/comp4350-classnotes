from gluon.validators import *
from gluon.dal import DAL, Field

import os

class DBContext:
    """ context for the database on web2py 

    stores all the state about currently defined tables, etc.
    passed to all accesssors when created, this is the link for common db code
    """

    def __init__(self, db_file, migrate_lambda=None):
        """ constructor.
        params:
            db_file - name of the file to put the database in
            migrate_lambda - lambda which accepts table name, returns filename to store migrate in
               default migrate lambda returns true all the time
        """
        self.db_file = db_file
        if migrate_lambda:
            self.migrate = migrate_lambda
        else:
            self.migrate = lambda table: True

        self.db = DAL("sqlite://%s" % self.db_file)
        
        # this is the default username table for the web2py auth module
        # I will define it explicitly here so we can make changes to it.
        # We can add fields to this no problems, however, the built-in auth module requires these fields at a minimum
        self.db.define_table(
            'users',
            Field('first_name', length=128, default='', requires=IS_NOT_EMPTY()),
            Field('last_name', length=128, default='', requires=IS_NOT_EMPTY()),
            Field('email', length=128, default='', unique=True),
            Field('password', 'password', length=512, readable=False, label='Password', requires=[IS_STRONG(), CRYPT()]),
            Field('registration_key', length=512, writable=False, readable=False, default=''),
            Field('reset_password_key', length=512, writable=False, readable=False, default=''),
            Field('registration_id', length=512, writable=False, readable=False, default=''),
            Field('role', 'integer', requires=IS_NOT_EMPTY()),
            migrate=self.migrate('users')
        )
        user_table = self.db['users']
        user_table.email.requires =[IS_EMAIL(), IS_NOT_IN_DB(self.db, user_table.email)]

        self.db.define_table('courses',
            Field('department', 'string', requires=IS_NOT_EMPTY()),
            Field('number', 'integer', requires=IS_NOT_EMPTY()),
            Field('section', 'string', requires=IS_NOT_EMPTY()),
            Field('instructor', 'string', requires=IS_NOT_EMPTY()),
            migrate=self.migrate('courses')
        )
        
        self.db.define_table('enrolled',
            Field('user_id', self.db.users, requires=IS_NOT_EMPTY()),
            Field('course_id', self.db.courses, requires=IS_NOT_EMPTY()),
            migrate=self.migrate('enrolled')
        )

        self.db.define_table('notes',
            Field('start_date', 'date', requires=[IS_NOT_EMPTY(),IS_DATE()]),
            Field('end_date', 'date', requires=[IS_NOT_EMPTY(),IS_DATE()]),
            Field('notes', 'upload', autodelete=True, requires=IS_NOT_EMPTY()), # must do autodelete to avoid polluting the db with old files
            Field('course_id', self.db.courses, requires=IS_NOT_EMPTY()), # foreign key relationship
            Field('created_by', 'integer'), # eventually make this a foreign key on user table
            Field('modified_by', 'integer'), # ditto
            Field('created_on', 'datetime'),
            Field('modified_on', 'datetime'),
            migrate=self.migrate('notes')
        )

    def close(self):
        """ using internal reference to db adapter, but its the only way to close... """
        self.db.commit()
        self.db._adapter.close()



    
 
   
    


