from app import application, db, login_manager
from extra_files import insert_extra_files


if __name__ == '__main__':
    login_manager.init_app(application)
    application.run(debug=True, extra_files=insert_extra_files())