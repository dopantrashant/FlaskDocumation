from app import app, db
from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user
from app.models import User
from app.forms import RegisterForm, LoginForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        employee = User.query.filter_by(roll_no=int(form.roll_no.data)).first()
        if employee is None or not employee.check_password(form.password.data):
            flash('Invalid Username or Password')
            return redirect(url_for('login'))
        login_user(employee, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        employee = User(employee_name=form.employee_name.data, email=form.email.data, roll_no=int(form.roll_no.data), branch_code=int(form.branch_code.data))
        employee.set_password(form.password.data)
        db.session.add(employee)
        db.session.commit()
        flash('Congratulations, you are not a registered user!')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

