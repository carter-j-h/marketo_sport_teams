from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
team = Table('team', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('team', VARCHAR(length=140)),
    Column('league', VARCHAR(length=140)),
    Column('user_id', INTEGER),
)

user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('email', VARCHAR(length=120)),
    Column('username', VARCHAR(length=64)),
)

Teams = Table('Teams', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('team', String(length=140)),
    Column('league', String(length=140)),
)

Users = Table('Users', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=64)),
    Column('email', String(length=120)),
)

summary = Table('summary', post_meta,
    Column('user_id', Integer),
    Column('team_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['team'].drop()
    pre_meta.tables['user'].drop()
    post_meta.tables['Teams'].create()
    post_meta.tables['Users'].create()
    post_meta.tables['summary'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['team'].create()
    pre_meta.tables['user'].create()
    post_meta.tables['Teams'].drop()
    post_meta.tables['Users'].drop()
    post_meta.tables['summary'].drop()
