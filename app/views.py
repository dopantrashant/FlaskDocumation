from werkzeug.urls import url_parse

from app import app, db
from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Branch, Customer
from app.forms import RegisterForm, LoginForm, CustomerForm, BranchForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    if current_user.is_authenticated:
        print(current_user.branch.percent_profile_complete())
        if current_user.branch.percent_profile_complete() < 80:
            form = BranchForm()
            if form.validate_on_submit():
                branch = current_user.branch
                branch.branch_name = form.branch_name.data.strip()
                branch.branch_address_line_1 = form.branch_address_line_1.data.strip()
                branch.branch_address_line_2 = form.branch_address_line_2.data.strip()
                branch.state = form.state.data.strip()
                branch.district = form.district.data.strip()
                branch.pin = form.pin.data.strip()
                branch.email = form.email.data.strip()
                branch.contact_number = form.contact_no.data.strip()
                db.session.add(branch)
                db.session.commit()
                flash("Congrates Branch data has been updated successfully.", category="success")
                return render_template('index.html')
            flash("Kindly Update the details of your branch before proceeding further.", category="danger")
            return render_template('add_branch_details.html', form=form)
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        employee = User.query.filter_by(roll_no=int(form.roll_no.data)).first()
        if employee is None or not employee.check_password(form.password.data):
            flash('Invalid Username or Password', category="danger")
            return redirect(url_for('login'))
        login_user(employee, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        branch = Branch.query.filter_by(branch_code=int(form.branch_code.data)).first()
        user = User.query.filter_by(roll_no=int(form.roll_no.data)).first()
        if branch is None:
            branch = Branch(branch_code=int(form.branch_code.data), branch_address_line_1='default')
            db.session.add(branch)
            db.session.commit()
        if user is None:
            user = User(employee_name=form.employee_name.data, email=form.email.data, roll_no=int(form.roll_no.data),
                        branch=branch)
            user.set_password(form.password.data)
            db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!', category="success")
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)


@login_required
@app.route('/addcustomer', methods=['GET', 'POST'])
def addcustomer(customer_already_present=None):
    form = CustomerForm()
    if form.validate_on_submit():
        customer = Customer.query.filter(
            (Customer.cbs_cif == form.cbs_cif.data) | (Customer.uidai_no == form.uidai_no.data)).first()
        if customer is None:
            customer = Customer(
                cbs_cif=form.cbs_cif.data,
                salutation=form.salutation.data,
                first_name=form.first_name.data,
                middle_name=form.middle_name.data,
                last_name=form.last_name.data,
                short_name=form.short_name.data,
                gender=form.gender.data,
                dob=form.dob.data,
                marital_status=form.marital_status.data,
                father_husband_name=form.father_husband_name.data,
                mother_name=form.mother_name.data,
                uidai_no=int(form.uidai_no.data),
                pan_no=form.pan_no.data,
                driving_licence=form.driving_licence.data,
                voter_id=form.voter_id.data,
                passport=form.passport.data
            )
            db.session.add(customer)
            db.session.commit()
            flash('Customer Added Successfully', category='success')
            return redirect(url_for('index'))
        customer_already_present = 'Customer data already present in our system  customer id-{} kindly use search ' \
                                   'facility to find the customer'.format(customer.cbs_cif)
        flash(customer_already_present,
              category='info')
        return redirect(url_for('index'))
    return render_template('add_customer.html', form=form)


@login_required
@app.route('/search_customer', methods=['GET', 'POST'])
def search_customer():
    form = CustomerForm()
    if form.validate_on_submit():
        print(form.uidai_no.data)

    return render_template('find_customer.html', form=form)


@login_required
@app.route('/modify_customer', methods=['GET', 'POST'])
def modify_customer():
    form = CustomerForm()
    if form.validate_on_submit():
        print(form.uidai_no.data)

    return render_template('modify_customer.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
