import sqlalchemy

from .db import metadata


protocols = sqlalchemy.Table(
    'protocols',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String),
)
