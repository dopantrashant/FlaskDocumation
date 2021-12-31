from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.fields.html5 import EmailField, DateField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

SALUTATION_LIST = [(0, 'Select Salutation'), ('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Ms.', 'Ms.'), ('Dr.', 'Dr.')]
MOBILE_TYPE = [(0, 'Select Mobile Type'), ('Mobile', 'Mobile'), ('Landline', 'Landline'), ('Office', 'Office')]
EMAIL_ID_TYPE = [(0, 'Select Email Id Type'), ('Personal', 'Personal'), ('Official', 'Official'), ('Communication', 'Communication')]
ADDRESS_TYPE = [(0, 'Select Address Type'), ('Residential', 'Residential'), ('Permanent', 'Permanent'), ('Communication', 'Communication'), ('Office', 'Office')]
ID_ADDRESS_PROOF_TYPE = [
    ('ADHAAR CARD', 'ADHAAR CARD'),
    ('Voter ID', 'Voter ID'),
    ('PAN', 'PAN'),
    ('Driving Licence', 'Driving Licence'),
    ('Passport', 'Passport')
]
GENDER = [(0, 'Select Gender'), ('Male', 'Male'), ('Female', 'Female'), ('Third Gender', 'Third Gender')]
MARITAL_STATUS = [(0, 'Select Marital Status'), ('Married', 'Married'), ('Unmarried', 'Unmarried'), ('Divorced','Divorced')]
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
            raise ValidationError('Your Email Id Already Found in System. If you have forgotten your password try to reset it.')


class CustomerForm(FlaskForm):
    cbs_cif = StringField('CBS CIF ID of Customer', validators=[DataRequired()])
    uidai_no = StringField('Aadhar No:', validators=[DataRequired()])
    pan_no = StringField('PAN No:')
    passport = StringField('Passport:')
    driving_licence = StringField('Driving License')
    voter_id = StringField('Voter ID:')
    salutation = SelectField('Salutation:', choices=SALUTATION_LIST)
    first_name = StringField('First Name:', validators=[DataRequired()])
    middle_name = StringField('Middle Name:')
    last_name = StringField('Last Name:')
    short_name = StringField('Short Name:', validators=[DataRequired()])
    dob = DateField('Date of Birth:', format='%Y-%m-%d')
    gender = SelectField('Gender', choices=GENDER)
    marital_status = SelectField('Marital Status', choices=MARITAL_STATUS)
    father_husband_name = StringField('Father/Spouse Name:', validators=[DataRequired()])
    mother_name = StringField('Mother Name:', validators=[DataRequired()])
    submit = SubmitField('Add Customer')


class ContactForm(FlaskForm):
    mobile_number = StringField('Mobile Number')
    mobile_number_type = SelectField('Salutation:', choices=MOBILE_TYPE)
    email_id = StringField('Email ID:')
    email_id_type = SelectField('Salutation:', choices=EMAIL_ID_TYPE)


class BranchForm(FlaskForm):
    branch_name = StringField('Branch Name', validators=[DataRequired()])
    branch_address_line_1 = StringField('Branch Address Line1:', validators=[DataRequired()])
    branch_address_line_2 = StringField('Branch Address Line2:', validators=[DataRequired()])
    state = SelectField('State:', choices=INDIAN_STATES)
    district = SelectField('District:', choices=[('', ''), ("Erode", "Erode")])
    pin = StringField('Pincode:', validators=[DataRequired()])
    email = StringField('Branch Email:')
    contact_no = StringField('Branch Contact No.:')
    submit = SubmitField('Save Branch Details!')


class AddressForm(FlaskForm):
    address_line_1 = StringField('Address Line1:', validators=[DataRequired()])
    address_line_2 = StringField('Address Line2:', validators=[DataRequired()])
    district = StringField('District:', validators=[DataRequired()])
    state = SelectField('State:', choices=INDIAN_STATES)
    pin = StringField('Pincode:', validators=[DataRequired()])
    address_type = SelectField('Address Type:', choices=ADDRESS_TYPE)




