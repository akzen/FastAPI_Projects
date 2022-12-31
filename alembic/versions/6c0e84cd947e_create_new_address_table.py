"""Create new address table

Revision ID: 6c0e84cd947e
Revises: d99b4283ce74
Create Date: 2022-11-24 15:48:20.699352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c0e84cd947e'
down_revision = 'd99b4283ce74'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('address',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('address1', sa.VARCHAR(length=200), nullable=False),
                    sa.Column('address2', sa.VARCHAR(length=200), nullable=False),
                    sa.Column('city', sa.VARCHAR(length=50), nullable=False),
                    sa.Column('state', sa.VARCHAR(length=25), nullable=False),
                    sa.Column('country', sa.VARCHAR(length=25), nullable=False),
                    sa.Column('postal_code', sa.Integer(), nullable=False))


def downgrade():
    op.drop_table('address')
