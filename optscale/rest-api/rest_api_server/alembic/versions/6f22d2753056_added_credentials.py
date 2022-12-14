""""added_credentials"

Revision ID: 6f22d2753056
Revises: 61039ec12750
Create Date: 2017-04-12 03:31:48.502957

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6f22d2753056'
down_revision = '61039ec12750'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vspherecredential',
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('state', sa.String(length=256), nullable=True),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('customer_id', sa.String(length=36), nullable=True),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.Column('endpoint', sa.String(length=256), nullable=False),
    sa.Column('username', sa.String(length=256), nullable=False),
    sa.Column('password', sa.LargeBinary(), nullable=False),
    sa.Column('salt', sa.String(length=36), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id']),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vspherecredential')
    # ### end Alembic commands ###
