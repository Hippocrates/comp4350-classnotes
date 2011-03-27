import os
import glob

from gluon.dal import DAL
from gluon.contrib.populate import populate

from applications.notes.modules.db.base import DBContext

class TestDBContext:
    """ Class to handle setting up / destroying test database context """
    init = 0
    db_context = None

    @staticmethod
    def init_db():
        assert TestDBContext.init == 0
        TestDBContext.init = 1

        TestDBContext.db_context = DBContext("test.sqlite", lambda table: "%s.test.migrate" % table)

        db = TestDBContext.db_context.db
        # populate test database with dummy data
        populate(db[DBContext.COURSE_TABLE], 100)
        populate(db[DBContext.NOTE_TABLE], 100)
        populate(db[DBContext.USER_TABLE], 10)
        populate(db[DBContext.ENROLLMENT_TABLE], 10)

    @staticmethod
    def wipe_db():
      """ called at the end of a test or block of tests to 
      clean up & reinitialize the db """
      assert TestDBContext.init == 1
      TestDBContext.init = 0
      #delete migration files and test database file
      path_to_db = os.path.join(os.getcwd(), 'applications', 'notes', 'databases')
      TestDBContext.db_context.close()
      os.unlink(os.path.join(path_to_db, TestDBContext.db_context.db_file))

      migrate_files = glob.glob(os.path.join(path_to_db, '*.test.migrate'))
      for file in migrate_files:
          os.unlink(file)

      TestDBContext.db_context = None


