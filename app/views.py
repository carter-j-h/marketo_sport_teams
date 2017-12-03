from flask import render_template, flash, redirect, session, url_for, request, g
from app import app, db, models, login_manager
from flask.ext.login import UserMixin, login_user, logout_user, current_user, login_required 
from .forms import LoginForm, RegistrationForm


@app.route('/index')

def index():    

    return render_template('index.html',
                           current_user=current_user)

@app.route('/base')
def base():
	return render_template('base.html')

# user loader callback userd to get the users id from the database
@login_manager.user_loader
def load_user(id):

    return models.User.query.get(int(id))

@app.route('/register', methods=['GET', 'POST'])

def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    user = models.User(email= form.email.data,
                        username = form.username.data,
                        password= form.password.data)
    db.session.add(user)
    db.session.commit()
    login_user(user)
    flash('Are we successful??')
    return redirect(request.args.get('next') or url_for('index'))
  return render_template ('register.html',
                          form= form)

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
      user = models.User.query.filter_by(email=form.email.data).first()
      if user is not None and user.verify_password(form.password.data):
        login_user(user)
        flash('You have logged in successfully!')
        return redirect(request.args.get('next') or url_for('index'))
        
    return render_template('login.html', 
                           title='Sign In',
                           form=form)

@app.route('/logout')
@login_required
def logout():
  logout_user()
  flash('You have been logged out.')
  return redirect(request.args.get('next') or url_for('/login'))

@app.route('/user/<username>')
def user(username):

  user = models.User.query.filter_by(username= username).first()


  if user == None:
    flash('User %s not found.' % username )
    return redirect(url_for('login'))

  teams = user.teams.all()

  return render_template('user.html',
                           user=user,
                           teams=teams)

@app.route('/results')
@login_required
def results():
  return render_template('results.html',
                          current_user=current_user)
