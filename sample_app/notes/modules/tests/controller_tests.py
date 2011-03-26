import unittest
import glob
import sys

from gluon.shell import exec_environment, env
from gluon.compileapp import build_environment
from gluon.globals import Request, Session, Storage, Response
from datetime import datetime

from applications.notes.modules.db.access.course_stub import CourseAccessorStub;
from applications.notes.modules.db.access.note_stub import NoteAccessorStub;

from applications.notes.modules.tests.db_test_module import TestDBContext

# To run this application, you need to run it from inside web2py.
# hence, with your current directory in the 'web2py' folder, run
# this command:
# > python web2py.py -S notes -M -R applications/notes/modules/tests/controller_tests.py

class ControllerTests(unittest.TestCase):
  def setUp(self):
    # Okay, this shit is bananas.  In order to be able to load the
    # web2py module with the right environment, I need to manually
    # specify all of these values as globals, and then re-build
    # them each time a test is run.  The execfile will only run
    # once, but it needs to run _after_ these have been specified
    # as globals, otherwise they will not be accessible properly
    # from the tests
    global request, session, response, access_note, access_course
    
    request = Request();
    session = Session();
    response = Response();
    access_note = NoteAccessorStub();
    access_course = CourseAccessorStub();

    # your setUp is being called > 1 per test. 
    # which breaks the testDBcontext. why does this happen?
    #access_note = NoteAccessor(TestDBContext.db_context)
    #access_course = CourseAccessor(TestDBContext.db_context)
    #TestDBContext.init_db()

    #exec_environment("applications/notes/controllers/default.py", globals())
    execfile("applications/notes/controllers/default.py", globals())
    pass;

  def tearDown(self):
    #TestDBContext.wipe_db()
    pass;

  # this is a helper method to grab the form name and form key
  # from a post form, so that we can actually submit
  # it takes a dictionary of the form inputs to be specified
  def makePostVars(self,**kwargs):
    emptyResult = search_notes();
    kwargs['_formkey'] = emptyResult['form'].formkey;
    kwargs['_formname'] = emptyResult['form'].formname;
    print(emptyResult['form'].formname);
    return Storage(kwargs);

  def testSearchPost(self):
    request.vars = self.makePostVars(dept='comp',number='1020');
    request.env.request_method = 'POST';
    
    result = search_notes();

    # check that the form submitted correctly
    self.assertFalse(result['form'].errors);
    self.assertFalse(result['results'] == None);

    # todo: check that the data returned is in the expected format

  def testFailedSearchPost(self):
    # just submit some random crap that will not be accepted
    request.vars = self.makePostVars(email='ddd');
    request.env.request_method = 'POST';

    result = search_notes();

    # check that the controller returned errors on the form and
    # that no data was returend
    self.assertTrue(result['form'].errors);
    self.assertTrue(result['results'] == None);
    
    
  def testSearch(self):
    #try finding a note added directly to the the DB
    request.vars = self.makePostVars(dept='comp',number='1020');
    request.env.request_method = 'POST';
    
    aNote = access_note.make_note_stub(0, datetime(1337, 1, 1), 1020, "user");
    added = access_note.insert_note(aNote);

    #*check that the note was added
    self.assertFalse(added == None);

    print("This is the id: " + str(added));

    re = access_note.get_note_list();

    print(str(re));

    result = search_notes();
    
    #*something* should have been returned...
    self.assertTrue(len(result['results']) > 0);
    
    #a note should have been returned with the course number we want
    foundNote = False;
    
    for someNote in result['results']:
      print(str(someNote));
      foundNote = foundNote or (someNote.course_id == 1020 and someNote.start_date == datetime(1337, 1, 1));
    self.assertTrue(foundNote, "Did not find the expected note in the search results");
    
    #*all* of the notes that have been returned should have the course number we want
    for someNote in result['results']:
      self.assertTrue(someNote.course_id == 1020, "Found notes in the search results that have the wrong course_id");
      
    
  #would like to do a submission + find (no direct DB access),
  #  need to figure out if I can manipulate the crud form
    

# entry point
def main():
  suite = unittest.TestLoader().loadTestsFromTestCase(ControllerTests);
  runner = unittest.TextTestRunner()
  runner.run(suite)


# run main
main();
