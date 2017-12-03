from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
summary = Table('summary', pre_meta,
    Column('user_id', INTEGER),
    Column('team_id', INTEGER),
)

Teams = Table('Teams', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('team', String(length=140)),
    Column('league', String(length=140)),
    Column('user_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['summary'].drop()
    post_meta.tables['Teams'].columns['user_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['summary'].create()
    post_meta.tables['Teams'].columns['user_id'].drop()
