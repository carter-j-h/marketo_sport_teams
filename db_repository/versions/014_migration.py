from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
Teams = Table('Teams', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('team', VARCHAR(length=140)),
    Column('league', VARCHAR(length=140)),
)

Users = Table('Users', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('username', VARCHAR(length=64)),
    Column('email', VARCHAR(length=120)),
)

team = Table('team', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('team', String(length=140)),
    Column('league', String(length=140)),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=64)),
    Column('email', String(length=120)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['Teams'].drop()
    pre_meta.tables['Users'].drop()
    post_meta.tables['team'].create()
    post_meta.tables['user'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['Teams'].create()
    pre_meta.tables['Users'].create()
    post_meta.tables['team'].drop()
    post_meta.tables['user'].drop()
