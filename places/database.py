from sqlalchemy import MetaData, Table, Column, UniqueConstraint, Integer, Float, String, Text, and_
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql import select

from places.extensions import db

metadata = MetaData(bind=db)

# SQL Table definitions
buildings = Table('buildings', metadata,
                  Column('b_id', String(8), primary_key=True),
                  Column('api_id', Text, nullable=False),
                  Column('name', Text, nullable=False),
                  Column('address', Text, nullable=False),
                  # TODO: should be renamed to "address2" in database - or db should have state field added.  Maybe even address1, address2 and state added?
                  Column('city', Text, nullable=False),
                  Column('zipcode', Text, nullable=False),
                  Column('image_url', Text, nullable=False),
                  Column('website_url', Text, nullable=False),
                  Column('longitude', Float, nullable=False),
                  Column('latitude', Float, nullable=False),
                  Column('shape_coordinates', Text, nullable=True),
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


def get_buildings():
    """
    Gets all buildings
    """
    query = buildings.select()
    return db.engine.execute(query)


def get_buildings_by_name(name):
    """
    Gets buildings matching the given name
    """
    query = select([buildings], buildings.c.name.like('%' + name + '%'))
    return db.engine.execute(query)


def get_buildings_by_category(category_name):
    """
    Gets buildings in the given category
    :param category_name: The name of the category
    """
    query = select([buildings, categories], and_(categories.c.cat_name == category_name, categories.c.b_id == buildings.c.b_id))
    return  db.engine.execute(query).fetchall()


def get_building(b_id):
    """
    Gets a building by ID
    :param b_id: The building ID
    """
    query = select([buildings], buildings.c.b_id == b_id)
    return db.engine.execute(query).fetchall()


def get_categories_for_building(b_id):
    """
    Get all the categories a building belongs to
    """
    query = select([categories.c.cat_name], categories.c.b_id ==  b_id).distinct()
    results = db.engine.execute(query).fetchall()
    categories_ret = []
    for res in results:
        categories_ret.append(res[0])
    return categories_ret


def get_tags_for_building(b_id):
    """
    Get all the tags a building is associated with
    """
    query = select([tags.c.tag_name], tags.c.b_id == b_id).distinct()
    results = db.engine.execute(query).fetchall()
    tags_ret = []
    for res in results:
        tags_ret.append(res[0])
    return tags_ret


def create_building(b_id, api_id, name, address, city, zipcode, image_url, website_url, longitude, latitude, shape_coordinates, phone_num):
    """Creates a new building in the database"""
    query = buildings.insert().values(
        b_id = b_id,
        api_id = api_id,
        name = name,
        address = address,
        city = city,
        zipcode = zipcode,
        image_url = image_url,
        website_url = website_url,
        longitude = longitude,
        latitude = latitude,
        shape_coordinates = shape_coordinates,
        phone_num = phone_num)
    db.engine.execute(query)


def get_tags():
    """
    Gets all tags
    """
    query = select([tags])
    return db.engine.execute(query)


def get_tag(name):
    """
    Gets tag by name.
    """
    query = select([tags.c.tag_id, tags.c.b_id, tags.c.tag_name, tags.c.gtuser, tags.c.auth, tags.c.times_tag, tags.c.flag_users, tags.c.times_flagged], and_(tags.c.tag_name.like('%' + name + '%'), tags.c.b_id == buildings.c.b_id))
    return db.engine.execute(query)


def create_tag(b_id, tag, gtuser):
    """
    Create a tag in the database
    :param b_id: Building ID
    :param tag: The tag
    :param gtuser: The user name of the GT user creating the tag
    """
    tag = "'"+tag+"'" # for some weird reason, each tag in the database is surrounded with single quotes

    try:  # SQLAlchemy does not have a ON DUPLICATE UPDATE method, this is the best workaround I found (Jayanth)
        query = tags.insert().values(b_id=b_id, tag_name=tag, gtuser=gtuser, auth=0, times_tag=1, flag_users='', times_flagged=0)
        db.engine.execute(query)
    except IntegrityError:
        query = tags.update(and_(tags.c.tag_name == tag, tags.c.b_id == b_id), values={tags.c.times_tag: tags.c.times_tag+1})
        db.engine.execute(query)


def flag_tag(id, gtuser):
    """
    Flag a tag as being incorrect.
    :param id: The tag ID
    :param gtuser: The username of the user flagging the tag
    """
    query = tags.update(tags.c.tag_id == id, values={tags.c.flag_users: tags.c.flag_users+cas.username+',', tags.c.times_flagged: tags.c.times_flagged+1})
    db.engine.execute(query)


def get_categories():
    """
    Gets all categories
    """
    query = select([categories.c.cat_name]).distinct()
    return db.engine.execute(query).fetchall()
