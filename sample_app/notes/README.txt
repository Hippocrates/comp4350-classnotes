I've setup a really basic notes database sample app for you guys to check out.

To install the application, just drop it into the 'applications' directory of web2py.

When you first run web2py, it will automatically open your web browser to the web2py welcome app.
Assuming the URL for the welcome app is http://127.0.0.1:8000/welcome , you could access this app by going to
http://127.0.0.1:8000/notes

Files you want to look at are:
	controllers/default.py => this is where i wrote some simple controller functions.
				  only pay attention to the index() and add_notes() functions

	views/layout.html => this is the template for all other views
	views/default/index.html => this is the view for controller default, function 'index'
	views/default/add_notes.html => this file actually doesn't exist. but the controller still generates output.
				        actually, since I haven't defined a view, web2py just uses the default one.
					as an excercise, see if you can override this with a custom view

	models/0_bootstrap.py => this is where we setup the web2py environment 
	models/menu.py => this is where the menu for the application is defined
	models/tables.py => this is where i defined some simple tables