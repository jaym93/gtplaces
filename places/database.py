from sqlalchemy import MetaData, Table, Column, UniqueConstraint, Integer, Float, String, Text
from sqlalchemy.sql import select

from places.extensions import db

metadata = MetaData(bind=db)

# SQL Table definitions
buildings = Table('buildings', metadata,
                  Column('b_id', String(8), primary_key=True),
                  Column('api_id', Text, nullable=False),
                  Column('name', Text, nullable=False),
                  Column('address', Text, nullable=False),
                  Column('city', Text, nullable=False),
                  Column('zipcode', Text, nullable=False),
                  Column('image_url', Text, nullable=False),
                  Column('website_url', Text, nullable=False),
                  Column('longitude', Float, nullable=False),
                  Column('latitude', Float, nullable=False),
                  Column('shape_coordinates', Text, nullable=False),
                  Column('phone_num', String(15), nullable=False)
                  )

categories = Table('categories', metadata,
                   Column('cat_id', Integer, primary_key=True),
                   Column('b_id', String(11), nullable=False),
                   Column('cat_name', Text, nullable=False)
                   )

tags = Table('tags', metadata,
             Column('tag_id', Integer, primary_key=True),
             Column('b_id', Text, nullable=False),
             Column('tag_name', Text, nullable=False),
             Column('gtuser', Text, nullable=False),
             Column('auth', Integer, nullable=False),
             Column('times_tag', Integer, nullable=False),
             Column('flag_users', Text, nullable=False),
             Column('times_flagged', Integer, nullable=False),
             UniqueConstraint('b_id', 'tag_name')
             )

flags = Table('flags', metadata,
              Column('flag_id', Integer, primary_key=True),
              Column('tag_id', Integer, nullable=False),
              Column('gtuser', Text, nullable=False)
              )


def create_tables():
    """
    Create database tables, if needed
    """
    metadata.create_all(db.engine)


def get_categories(b_id):
    """
    Get all the categories a building belongs to
    """
    query = select([categories.c.cat_name], categories.c.b_id ==  b_id).distinct()
    results = db.engine.execute(query).fetchall()
    categories_ret = []
    for res in results:
        categories_ret.append(res[0])
    return categories_ret


def get_tags(b_id):
    """
    Get all the tags a building is associated with
    """
    query = select([tags.c.tag_name], tags.c.b_id == b_id).distinct()
    results = db.engine.execute(query).fetchall()
    tags_ret = []
    for res in results:
        tags_ret.append(res[0])
    return tags_ret

