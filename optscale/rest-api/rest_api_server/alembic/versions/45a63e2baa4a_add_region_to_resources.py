""""add region to resources"

Revision ID: 45a63e2baa4a
Revises: c766962faf4f
Create Date: 2020-07-24 10:50:58.617993

"""
import os

import config_client.client
from pymongo import MongoClient

from alembic import op
import sqlalchemy as sa
from sqlalchemy import table, column, update
from sqlalchemy.orm import Session

DEFAULT_ETCD_HOST = 'etcd-client'
DEFAULT_ETCD_PORT = 80

# revision identifiers, used by Alembic.
revision = '45a63e2baa4a'
down_revision = 'c766962faf4f'
branch_labels = None
depends_on = None


def _get_etcd_config_client():
    etcd_host = os.environ.get('HX_ETCD_HOST', DEFAULT_ETCD_HOST)
    etcd_port = os.environ.get('HX_ETCD_PORT', DEFAULT_ETCD_PORT)
    config_cl = config_client.client.Client(host=etcd_host, port=int(etcd_port))
    return config_cl


def _get_mongo(config_cl):
    mongo_params = config_cl.mongo_params()
    mongo_conn_string = "mongodb://%s:%s@%s:%s" % mongo_params[:-1]
    mongo_client = MongoClient(mongo_conn_string)
    return mongo_client.restapi.expenses


def get_regions_map_from_mongo():
    config_cl = _get_etcd_config_client()
    mongo_cl = _get_mongo(config_cl)
    pipeline = [
        {'$group': {
            '_id': "$resource_id",
            'region': {'$first': '$region'}
        }}
    ]
    return mongo_cl.aggregate(pipeline)


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('resource', sa.Column('region', sa.String(length=255),
                                        nullable=True))
    bind = op.get_bind()
    session = Session(bind=bind)
    table_ = table('resource',
                   column('id', sa.String(36)),
                   column('region', sa.String(length=255)))
    regions_map = get_regions_map_from_mongo()
    for item in regions_map:
        upd_stmt = update(
            table_
        ).values(
            region=item["region"]
        ).where(table_.c.id == item["_id"])
        session.execute(upd_stmt)
    try:
        session.commit()
    finally:
        session.close()
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('resource', 'region')
    # ### end Alembic commands ###
