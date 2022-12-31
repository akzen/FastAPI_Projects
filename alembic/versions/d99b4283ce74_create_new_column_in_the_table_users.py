"""create new column in the table users.

Revision ID: d99b4283ce74
Revises: 
Create Date: 2022-11-24 15:39:26.228339

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd99b4283ce74'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('phone_number', sa.VARCHAR(length=10), nullable=True))


def downgrade():
    op.drop_column('users', 'phone_number')
