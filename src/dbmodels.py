from datetime import datetime

from sqlalchemy import Table, MetaData, Column, Integer, String, Text, DateTime, Boolean

metadata = MetaData()

TodoItemInDB = Table(
    'todo', metadata,
    Column('id', Integer, autoincrement=True, primary_key=True),
    Column('title', String(100), nullable=False),
    Column('done', Boolean),
    Column('description', Text),
    Column('created_at', DateTime),
    Column('updated_at', DateTime, onupdate=datetime.now())
)
