from run import application
import flask
from app.models import *
from app.forms import LoginForm

@application.route('/')
def index():
    return flask.render_template('index.html')


@application.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return flask.render_template('login.html', 
                           title='Sign In',
                           form=form)
# @application.route("/logout")
# @login_required
# def logout():
#     logout_user()
#     return redirect('/')