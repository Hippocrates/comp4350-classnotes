# all the variables defined here become global, and can be access from any model or view
# thus, every model is executed implicitly at each page load 
# models are executed in alphabetical order, this one needs to run first,
# hence the 0_ part of its name.

# import the "glue" we will build our app with
from gluon.tools import *

DBContext = local_import("db/base", True).DBContext

# setup the db context and pull a reference to the actual database into globals
# for compatibility with web2py
db_context = DBContext("storage.sqlite")
db = db_context.db 

# setup mail object used for sending mail 
mail = Mail()                                		  # object used to send email 
mail.settings.server = 'logging' or 'smtp.gmail.com:587'  # your SMTP server
mail.settings.sender = 'you@gmail.com'         		  # your email
mail.settings.login = 'username:password'      		  # your credentials or None

# setup auth object for allowing users to register/login
auth = Auth(globals(),db)                      # object with handles authentication
auth.settings.hmac_key = 'sha512:88c35b00-2555-4e6f-b79d-063d724706f7' # set private key for hmac in the application

# this is the default username table for the web2py auth module
# I will define it explicitly here so we can make changes to it.
# We can add fields to this no problems, however, the built-in auth module requires these fields at a minimum
db.define_table(
    auth.settings.table_user_name,
    Field('first_name', length=128, default='', requires=IS_NOT_EMPTY(error_message=auth.messages.is_empty)),
    Field('last_name', length=128, default='', requires=IS_NOT_EMPTY(error_message=auth.messages.is_empty)),
    Field('email', length=128, default='', unique=True),
    Field('password', 'password', length=512, readable=False, label='Password', requires=[IS_STRONG(), CRYPT()]),
    Field('registration_key', length=512, writable=False, readable=False, default=''),
    Field('reset_password_key', length=512, writable=False, readable=False, default=''),
    Field('registration_id', length=512, writable=False, readable=False, default='')
)
user_table = db[auth.settings.table_user_name]
user_table.email.requires =[IS_EMAIL(error_message=auth.messages.invalid_email),
			    IS_NOT_IN_DB(db, user_table.email)]

auth.settings.table_user = user_table 
auth.define_tables()                           # creates all needed tables that we haven't defined yet
auth.settings.mailer = mail                    # for user email verification, turned off for now

auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.messages.verify_email = 'Click on the link http://'+request.env.http_host+URL('default','user',args=['verify_email'])+'/%(key)s to verify your email'
auth.settings.reset_password_requires_verification = True
auth.messages.reset_password = 'Click on the link http://'+request.env.http_host+URL('default','user',args=['reset_password'])+'/%(key)s to reset your password'

# setup crud object for simplified Create Retrieve Update Delete operations on the database
crud = Crud(globals(),db)                      # used to simplify Create Retrieve Update Delete operations
crud.settings.auth = None                      # auth to enforce authorization on crud
