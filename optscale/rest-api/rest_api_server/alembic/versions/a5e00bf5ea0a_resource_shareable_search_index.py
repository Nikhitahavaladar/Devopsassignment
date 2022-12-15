""""resource_shareable_search_index"

Revision ID: a5e00bf5ea0a
Revises: 6aa910d014f7
Create Date: 2021-08-27 17:30:18.110421

"""
import os
from pymongo import MongoClient
from config_client.client import Client as EtcdClient

# revision identifiers, used by Alembic.
revision = 'a5e00bf5ea0a'
down_revision = '6aa910d014f7'
branch_labels = None
depends_on = None
DEFAULT_ETCD_HOST = 'etcd-client'
DEFAULT_ETCD_PORT = 80
INDEX_NAME = 'ShareableResource'


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
    resources_collection = _get_resources_collection()
    resources_collection.create_index([('shareable', 1)], name=INDEX_NAME)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    resources_collection = _get_resources_collection()
    indexes = [x['name'] for x in resources_collection.list_indexes()]
    if INDEX_NAME in indexes:
        resources_collection.drop_index(INDEX_NAME)
    # ### end Alembic commands ###
