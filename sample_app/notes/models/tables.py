#########################################################################
## Define tables for example:
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
########################################################################
# note, each table gets an ID field automatically

user_table = db[auth.settings.table_user_name]


# define some base fields that we can import into any table
name_field = Field('name', 'string', requires=IS_NOT_EMPTY())
current_user = db.auth.user.id if auth.is_logged_in() else 0
created_by = Field('created_by', user_table, default=current_user, readable=False, writable=False)
created_on = Field('created_on', 'datetime', default=request.now, readable=False, writable=False)
modified_by = Field('modified_by', user_table, default=current_user, update=current_user, readable=False, writable=False)
modified_on = Field('modified_on', 'datetime', default=request.now, update=request.now, readable=False, writable=False)


# here we define 4 simple tables
# the relationship here may need to be adjusted as we go

db.define_table('instructors',
	Field('name', 'string', requires=IS_NOT_EMPTY()),
	# when another table uses instructors as a foreign key
	# this is used to define what is displayed
	# as the text of the dropdown for each row of instructors 
	format='%(name)s'
)

db.define_table('courses',
	Field('name', 'string', requires=IS_NOT_EMPTY()),
	format='%(name)s'
)

db.define_table('sections',
	Field('name', 'string', requires=IS_NOT_EMPTY()),
	Field('instructor', db.instructors), # forein key relationship
	Field('course',	db.courses),
	format="%(course)s"
)

# not linked into instructors/courses/sections yet 
# exercise: can you add this?
db.define_table('notes',
	Field('start_date', 'date', requires=[IS_NOT_EMPTY(),IS_DATE()]),
	Field('end_date', 'date', requires=[IS_NOT_EMPTY(),IS_DATE()]),
	Field('notes', 'upload', requires=IS_NOT_EMPTY()),
	created_by,
	created_on,
	modified_by,
	modified_on
)
