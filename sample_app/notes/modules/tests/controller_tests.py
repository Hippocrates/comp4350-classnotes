import unittest
import glob
import sys

from gluon.shell import exec_environment, env
from gluon.compileapp import build_environment
from gluon.globals import Request, Session, Storage, Response

from applications.notes.modules.db.access.course_stub import AccessCourseStub;
from applications.notes.modules.db.access.note_stub import AccessNoteStub;

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
    access_note = AccessNoteStub();
    access_course = AccessCourseStub();
    execfile("applications/notes/controllers/default.py", globals())
    pass;

  def tearDown(self):
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

  def testSubmit(self):
    request.vars = self.makePostVars(dept='comp',number='1020');
    request.env.request_method = 'POST';
    
    result = search_notes();

    # check that the form submitted correctly
    self.assertFalse(result['form'].errors);
    self.assertFalse(result['results'] == None);

    # todo: check that the data returned is in the expected format

  def testFailedSubmit(self):
    # just submit some random crap that will not be accepted
    request.vars = self.makePostVars(email='ddd');
    request.env.request_method = 'POST';

    result = search_notes();

    # check that the controller returned errors on the form and
    # that no data was returend
    self.assertTrue(result['form'].errors);
    self.assertTrue(result['results'] == None);
    

# entry point
def main():
  suite = unittest.TestLoader().loadTestsFromTestCase(ControllerTests);
  runner = unittest.TextTestRunner()
  runner.run(suite)


# run main
main();
