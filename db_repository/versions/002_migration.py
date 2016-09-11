from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
character_metadata = Table('character_metadata', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('character', String(length=1)),
    Column('color', Integer),
    Column('colorHex', String(length=6)),
    Column('count', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['character_metadata'].columns['colorHex'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['character_metadata'].columns['colorHex'].drop()
