""""migration_script"

Revision ID: d56f9da1f7bd
Revises: 86a9064bd530
Create Date: 2017-10-30 14:44:29.976844

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd56f9da1f7bd'
down_revision = '8beda2f3740a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('script',
    sa.Column('deleted_at', sa.Integer(), nullable=False),
    sa.Column('id', sa.String(36), nullable=False),
    sa.Column('script', sa.TEXT(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('customer_id', sa.String(36), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('script')
    # ### end Alembic commands ###
