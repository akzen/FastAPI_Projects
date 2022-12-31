"""Create address_id to the users.

Revision ID: ce6cc5c0f3db
Revises: 6c0e84cd947e
Create Date: 2022-11-24 16:07:14.363740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce6cc5c0f3db'
down_revision = '6c0e84cd947e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column("address_id", sa.Integer(), nullable=True))
    op.create_foreign_key('address_users_fk', source_table='users', referent_table='address', 
                          local_cols=['address_id'], remote_cols=['id'], ondelete='CASCADE')


def downgrade():
    op.drop_constraint('address_users_fk', table_name='users')
    op.drop_column('users', 'address_id')
