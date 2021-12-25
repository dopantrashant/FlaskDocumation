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
    addresses = db.relationship('Address', backref='person', lazy=True)
    contact = db.relationship('Contact', backref='person', lazy=True)
    id_address_proof = db.relationship('IdentityAddressProof', backref='person', lazy=True)


class IdentityAddressProof(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_type = db.Column(db.String(32))
    id_number = db.Column(db.String(32), unique=True)
    is_valid_address_proof = db.Column(db.Boolean, default=False)
    is_valid_id_proof = db.Column(db.Boolean, default=True)
    valid_from = db.Column(db.Date)
    valid_upto = db.Column(db.Date)
    issued_place = db.Column(db.String(64))
    person_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mobile_number = db.Column(db.String(10))
    mobile_number_type = db.Column(db.String(32))
    email_id = db.Column(db.String(128))
    email_id_type = db.Column(db.String(32))
    person_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address_line_1 = db.Column(db.String(64), nullable=False)
    address_line_2 = db.Column(db.String(64))
    address_line_3 = db.Column(db.String(64))
    address_line_4 = db.Column(db.String(64))
    district = db.Column(db.String(32))
    state = db.Column(db.String(64))
    pin = db.Column(db.String(6))
    address_type = db.Column(db.String(32))
    person_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)


class Branch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    branch_code = db.Column(db.Integer, unique=True)
    branch_name = db.Column(db.String(64))
    branch_address_line_1 = db.Column(db.String(64), nullable=False)
    branch_address_line_2 = db.Column(db.String(64))
    branch_address_line_3 = db.Column(db.String(64))
    branch_address_line_4 = db.Column(db.String(64))
    district = db.Column(db.String(32))
    state = db.Column(db.String(64))
    pin = db.Column(db.String(6))
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
        if self.branch_address_line_3 is not None:
            score += 10
        if self.branch_address_line_4 is not None:
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
