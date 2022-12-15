""""schedule_added_last_error"

Revision ID: 8bac85a6b1f9
Revises: 99f16ba3b402
Create Date: 2017-04-20 09:37:36.178768

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8bac85a6b1f9'
down_revision = '50c606a2bb38'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('schedule', sa.Column('last_error', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('schedule', 'last_error')
    # ### end Alembic commands ###
