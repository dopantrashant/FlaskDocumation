from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.fields.html5 import EmailField, DateField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

SALUTATION_LIST = [('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Ms.', 'Ms.'), ('Dr.', 'Dr.')]
MOBILE_TYPE = [('Mobile', 'Mobile'), ('Landline', 'Landline'), ('Office', 'Office')]
EMAIL_ID_TYPE = [('Personal', 'Personal'), ('Official', 'Official'), ('Communication', 'Communication')]
ADDRESS_TYPE = [('Residential', 'Residential'), ('Permanent', 'Permanent'), ('Communication', 'Communication'), ('Office', 'Office')]
ID_ADDRESS_PROOF_TYPE = [
    ('ADHAAR CARD', 'ADHAAR CARD'),
    ('Voter ID', 'Voter ID'),
    ('PAN', 'PAN'),
    ('Driving Licence', 'Driving Licence'),
    ('Passport', 'Passport')
]
INDIAN_STATES = [
    ("Andhra Pradesh", "Andhra Pradesh"),
    ("Andaman and Nicobar Islands"," Andaman and Nicobar Islands"),
    ("Arunachal Pradesh", "Arunachal Pradesh"),
    ("Assam", "Assam"),
    ("Bihar", "Bihar"),
    ("Chandigarh", "Chandigarh"),
    ("Chhattisgarh", "Chhattisgarh"),
    ("Dadar and Nagar Haveli", "Dadar and Nagar Haveli"),
    ("Daman and Diu", "Daman and Diu"),
    ("Delhi", "Delhi"),
    ("Lakshadweep", "Lakshadweep"),
    ("Puducherry", "Puducherry"),
    ("Goa", "Goa"),
    ("Gujarat", "Gujarat"),
    ("Haryana", "Haryana"),
    ("Himachal Pradesh", "Himachal Pradesh"),
    ("Jammu and Kashmir", "Jammu and Kashmir"),
    ("Jharkhand", "Jharkhand"),
    ("Karnataka", "Karnataka"),
    ("Kerala", "Kerala"),
    ("Madhya Pradesh", "Madhya Pradesh"),
    ("Maharashtra", "Maharashtra"),
    ("Manipur", "Manipur"),
    ("Meghalaya", "Meghalaya"),
    ("Mizoram", "Mizoram"),
    ("Nagaland", "Nagaland"),
    ("Odisha", "Odisha"),
    ("Punjab", "Punjab"),
    ("Rajasthan", "Rajasthan"),
    ("Sikkim", "Sikkim"),
    ("Tamil Nadu", "Tamil Nadu"),
    ("Telangana", "Telangana"),
    ("Tripura", "Tripura"),
    ("Uttar Pradesh", "Uttar Pradesh"),
    ("Uttarakhand", "Uttarakhand"),
    ("West Bengal", "West Bengal")
]


class LoginForm(FlaskForm):
    roll_no = IntegerField('Roll No:', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    employee_name = StringField('Employee Name:', validators=[DataRequired()])
    email = EmailField('Email:', validators=[DataRequired(), Email()])
    roll_no = StringField('Roll No:', validators=[DataRequired()])
    branch_code = StringField('Branch Code:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, roll_no):
        employee = User.query.filter_by(roll_no=int(roll_no.data)).first()
        if employee is not None:
            raise ValidationError('Your Roll No Already Found In System. If you have forgotten your password try to reset it.')

    def validate_email(self, email):
        employee = User.query.filter_by(email=email.data).first()
        if employee is not None:
            raise  ValidationError('Your Email Id Already Found in System. If you have forgotten your password try to reset it.')


class CustomerForm(FlaskForm):
    salutation = SelectField('Salutation:', choices=SALUTATION_LIST)
    first_name = StringField('First Name:', validators=[DataRequired()])
    middle_name = StringField('Middle Name:')
    last_name = StringField('Last Name:')
    short_name = StringField('Short Name:', validators=[DataRequired()])
    dob = DateField('Date of Birth:', format='%Y-%m-%d')
    father_husband_name = StringField('Father/Spouse Name:', validators=[DataRequired()])
    mother_name = StringField('Mother Name:', validators=[DataRequired()])


class ContactForm(FlaskForm):
    mobile_number = StringField('Mobile Number')
    mobile_number_type = SelectField('Salutation:', choices=MOBILE_TYPE)
    email_id = StringField('Email ID:')
    email_id_type = SelectField('Salutation:', choices=EMAIL_ID_TYPE)


class AddressForm(FlaskForm):
    address_line_1 = StringField('Address Line1:', validators=[DataRequired()])
    address_line_2 = StringField('Address Line2:', validators=[DataRequired()])
    address_line_3 = StringField('Address Line3:', validators=[DataRequired()])
    address_line_4 = StringField('Address Line4:', validators=[DataRequired()])
    district = StringField('District:', validators=[DataRequired()])
    state = SelectField('State:', choices=INDIAN_STATES)
    pin = StringField('Pincode:', validators=[DataRequired()])
    address_type = SelectField('Address Type:', choices=ADDRESS_TYPE)


class IdentityAddressProof(FlaskForm):
    id_type = SelectField('ID Type', choices=ID_ADDRESS_PROOF_TYPE)
    id_number = StringField('ID Proof Number:', validators=[DataRequired()])
    is_valid_address_proof = BooleanField('Is Valid Address Proof')
    is_valid_id_proof = BooleanField('Is Valid Id Proof')
    valid_from = DateField('Valid From:', format='%Y-%m-%d')
    valid_upto = DateField('Valid Upto:', format='%Y-%m-%d')
    issued_place = StringField('Issued Place:', validators=[DataRequired()])

