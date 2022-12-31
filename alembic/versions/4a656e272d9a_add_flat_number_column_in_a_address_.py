"""Add Flat number column in a address table.

Revision ID: 4a656e272d9a
Revises: ce6cc5c0f3db
Create Date: 2022-11-24 18:25:37.263801

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a656e272d9a'
down_revision = 'ce6cc5c0f3db'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('address', sa.Column('flat_no', sa.VARCHAR(length=10), nullable=True))


def downgrade():
    op.drop_column('address', 'flat_no')
