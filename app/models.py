from datetime import date
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(128), index=True, unique=True)
    roll_no = db.Column(db.Integer, unique=True)
    branch_code = db.Column(db.Integer, db.ForeignKey('branch.branch_code'))
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User Roll No {}'.format(self.roll_no)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cbs_cif = db.Column(db.String(12), unique=True)
    salutation = db.Column(db.String(10))
    first_name = db.Column(db.String(64), index=True)
    middle_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    full_name = db.Column(db.String(128))
    short_name = db.Column(db.String(64))
    gender = db.Column(db.String(64))
    dob = db.Column(db.Date)
    marital_status = db.Column(db.String(32))
    father_husband_name = db.Column(db.String(128))
    mother_name = db.Column(db.String(128))
    uidai_no = db.Column(db.String(12), unique=True)
    pan_no = db.Column(db.String(10), unique=True)
    driving_licence = db.Column(db.String(32), unique=True)
    voter_id = db.Column(db.String(32), unique=True)
    passport = db.Column(db.String(32))
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))
    mobile_numbers = db.relationship('MobileNumber', backref='customer', lazy=True)
    email = db.relationship('Email', backref='customer', lazy=True)

    def __init__(
            self,
            cbs_cif,
            salutation,
            first_name,
            middle_name,
            last_name,
            short_name,
            gender,
            dob,
            marital_status,
            father_husband_name,
            mother_name,
            uidai_no,
            pan_no,
            driving_licence,
            voter_id,
            passport
                    ):
        self.cbs_cif = cbs_cif
        self.salutation = salutation
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.short_name = short_name
        self.full_name = salutation+' '+first_name+' '+middle_name+' '+last_name
        self.gender = gender
        self.dob = dob
        self.marital_status = marital_status
        self.father_husband_name = father_husband_name
        self.mother_name = mother_name
        self.uidai_no = uidai_no
        self.pan_no = pan_no
        self.driving_licence = driving_licence
        self.voter_id = voter_id
        self.passport = passport

    def __repr__(self):
        return "<{} has cbs cif {}".format(self.full_name, self.cbs_cif)

    def age(self):
        today = date.today()
        dob = self.dob
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age

    def so_do_wo(self):
        pass


class MobileNumber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mobile_number = db.Column(db.String(10))
    mobile_number_type = db.Column(db.String(32))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)


class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64))
    email_type = db.Column(db.String(32))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address_line_1 = db.Column(db.String(64), nullable=False)
    address_line_2 = db.Column(db.String(64))
    address_line_3 = db.Column(db.String(64))
    address_line_4 = db.Column(db.String(64))
    district = db.Column(db.String(32))
    state = db.Column(db.String(64))
    pin = db.Column(db.String(6))


class Branch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    branch_code = db.Column(db.Integer, unique=True)
    branch_name = db.Column(db.String(64))
    branch_address_line_1 = db.Column(db.String(64), nullable=False)
    branch_address_line_2 = db.Column(db.String(64))
    district = db.Column(db.String(32))
    state = db.Column(db.String(64))
    pin = db.Column(db.String(6))
    ifsc = db.Column(db.String(11))
    micr = db.Column(db.Integer)
    contact_number = db.Column(db.String(16))
    email = db.Column(db.String(64))
    employees = db.relationship('User', backref='branch', lazy=True)

    def percent_profile_complete(self):
        score = 0
        if self.branch_name is not None:
            score += 10
        if self.branch_address_line_1 is not None:
            score += 10
        if self.branch_address_line_2 is not None:
            score += 10
        if self.district is not None:
            score += 10
        if self.state is not None:
            score += 10
        if self.pin is not None:
            score += 10
        if self.email is not None:
            score += 10
        if self.contact_number is not None:
            score += 10
        return score


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
