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

        self.db.define_table('courses',
            Field('department', 'string', requires=IS_NOT_EMPTY()),
            Field('number', 'integer', requires=IS_NOT_EMPTY()),
            Field('section', 'string', requires=IS_NOT_EMPTY()),
            Field('instructor', 'string', requires=IS_NOT_EMPTY()),
            migrate=self.migrate('courses')
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



    
 
   
    


