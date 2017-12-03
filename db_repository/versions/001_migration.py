from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
MLB_Teams = Table('MLB_Teams', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('team', VARCHAR(length=140)),
    Column('rank', SMALLINT),
    Column('timestamp', DATETIME),
    Column('user_id', INTEGER),
)

NBA_Teams = Table('NBA_Teams', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('team', VARCHAR(length=140)),
    Column('rank', SMALLINT),
    Column('timestamp', DATETIME),
    Column('user_id', INTEGER),
)

NFL_Teams = Table('NFL_Teams', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('team', VARCHAR(length=140)),
    Column('rank', SMALLINT),
    Column('timestamp', DATETIME),
    Column('user_id', INTEGER),
)

NHL_Teams = Table('NHL_Teams', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('team', VARCHAR(length=140)),
    Column('rank', SMALLINT),
    Column('timestamp', DATETIME),
    Column('user_id', INTEGER),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['MLB_Teams'].drop()
    pre_meta.tables['NBA_Teams'].drop()
    pre_meta.tables['NFL_Teams'].drop()
    pre_meta.tables['NHL_Teams'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['MLB_Teams'].create()
    pre_meta.tables['NBA_Teams'].create()
    pre_meta.tables['NFL_Teams'].create()
    pre_meta.tables['NHL_Teams'].create()
