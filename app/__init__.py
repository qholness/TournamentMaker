from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_login import LoginManager


application = Flask(__name__)
application.config.from_object('config')
bootstrap = Bootstrap(application)
mail = Mail(application)
login_manager = LoginManager()


# application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
# # application.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# # application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# # application.config['NO_BACKSLASH_ESCAPES'] = True

db = SQLAlchemy(application, 
	session_options={
		'expire_on_commit' : False,
	})

# db.create_all()


from app import views