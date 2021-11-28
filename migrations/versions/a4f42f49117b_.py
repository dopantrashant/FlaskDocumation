"""empty message

Revision ID: a4f42f49117b
Revises: 
Create Date: 2021-09-26 10:19:46.328689

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4f42f49117b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('salutation', sa.String(length=10), nullable=True),
    sa.Column('first_name', sa.String(length=64), nullable=True),
    sa.Column('middle_name', sa.String(length=64), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=True),
    sa.Column('full_name', sa.String(length=128), nullable=True),
    sa.Column('short_name', sa.String(length=64), nullable=True),
    sa.Column('dob', sa.Date(), nullable=True),
    sa.Column('father_husband_name', sa.String(length=128), nullable=True),
    sa.Column('mother_name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_customer_first_name'), 'customer', ['first_name'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('employee_name', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('roll_no', sa.Integer(), nullable=True),
    sa.Column('branch_code', sa.Integer(), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('roll_no')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_employee_name'), 'user', ['employee_name'], unique=False)
    op.create_table('address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('address_line_1', sa.String(length=64), nullable=False),
    sa.Column('address_line_2', sa.String(length=64), nullable=True),
    sa.Column('address_line_3', sa.String(length=64), nullable=True),
    sa.Column('address_line_4', sa.String(length=64), nullable=True),
    sa.Column('district', sa.String(length=32), nullable=True),
    sa.Column('state', sa.String(length=64), nullable=True),
    sa.Column('pin', sa.String(length=6), nullable=True),
    sa.Column('address_type', sa.String(length=32), nullable=True),
    sa.Column('person_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['person_id'], ['customer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contact',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mobile_number', sa.String(length=10), nullable=True),
    sa.Column('mobile_number_type', sa.String(length=32), nullable=True),
    sa.Column('email_id', sa.String(length=128), nullable=True),
    sa.Column('email_id_type', sa.String(length=32), nullable=True),
    sa.Column('person_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['person_id'], ['customer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('identity_address_proof',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_type', sa.String(length=32), nullable=True),
    sa.Column('id_number', sa.String(length=32), nullable=True),
    sa.Column('is_valid_address_proof', sa.Boolean(), nullable=True),
    sa.Column('is_valid_id_proof', sa.Boolean(), nullable=True),
    sa.Column('valid_from', sa.Date(), nullable=True),
    sa.Column('valid_upto', sa.Date(), nullable=True),
    sa.Column('issued_place', sa.String(length=64), nullable=True),
    sa.Column('person_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['person_id'], ['customer.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id_number')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('identity_address_proof')
    op.drop_table('contact')
    op.drop_table('address')
    op.drop_index(op.f('ix_user_employee_name'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_customer_first_name'), table_name='customer')
    op.drop_table('customer')
    # ### end Alembic commands ###
