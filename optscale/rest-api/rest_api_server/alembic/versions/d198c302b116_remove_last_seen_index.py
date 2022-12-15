""""remove_last_seen_index"

Revision ID: d198c302b116
Revises: 02a9af761e4e
Create Date: 2021-12-10 07:55:29.749487

"""
import os
from config_client.client import Client as EtcdClient
from pymongo import MongoClient

# revision identifiers, used by Alembic.
revision = 'd198c302b116'
down_revision = '02a9af761e4e'
branch_labels = None
depends_on = None

DEFAULT_ETCD_HOST = 'etcd-client'
DEFAULT_ETCD_PORT = 80
INDEX_NAME = 'LastSeen'
INDEX_KEY = 'last_seen'


def _get_etcd_config_client():
    etcd_host = os.environ.get('HX_ETCD_HOST', DEFAULT_ETCD_HOST)
    etcd_port = os.environ.get('HX_ETCD_PORT', DEFAULT_ETCD_PORT)
    config_cl = EtcdClient(host=etcd_host, port=int(etcd_port))
    return config_cl


def _get_resources_collection():
    config_cl = _get_etcd_config_client()
    mongo_params = config_cl.mongo_params()
    mongo_conn_string = "mongodb://%s:%s@%s:%s" % mongo_params[:-1]
    mongo_client = MongoClient(mongo_conn_string)
    return mongo_client.restapi.resources

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    mongo_resources = _get_resources_collection()
    index_names = {x['name'] for x in mongo_resources.list_indexes()}
    if INDEX_NAME in index_names:
        mongo_resources.drop_index(INDEX_NAME)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    mongo_resources = _get_resources_collection()
    index_names = {x['name'] for x in mongo_resources.list_indexes()}
    if INDEX_NAME not in index_names:
        mongo_resources.create_index(
            [(INDEX_KEY, 1)],
            name=INDEX_NAME,
            background=True
        )
    # ### end Alembic commands ###
