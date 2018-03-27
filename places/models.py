"""
Database models

See SQL Alchemy documentation:
http://flask-sqlalchemy.pocoo.org/2.3/
http://docs.sqlalchemy.org/en/latest/
"""
from sqlalchemy import String, Text, Float, Integer, UniqueConstraint, ForeignKey, cast
from sqlalchemy.orm import remote, foreign

from places.extensions import db


class Building(db.Model):
    """
    DB model representing a building
    """
    __tablename__ = 'buildings'

    b_id = db.Column('b_id', String(8), primary_key=True)
    api_id = db.Column('api_id', Text, nullable=False)
    name = db.Column('name', Text, nullable=False)
    address = db.Column('address', Text, nullable=False)
    # TODO: should be renamed to "address2" in database - or db should have state field added.  Maybe even address1, address2 and state added?
    city = db.Column('city', Text, nullable=False)
    zipcode = db.Column('zipcode', Text, nullable=False)
    image_url = db.Column('image_url', Text, nullable=False)
    website_url = db.Column('website_url', Text, nullable=False)
    longitude = db.Column('longitude', Float, nullable=False)
    latitude = db.Column('latitude', Float, nullable=False)
    shape_coordinates = db.Column('shape_coordinates', Text, nullable=True)
    phone_num = db.Column('phone_num', String(15), nullable=False)

    # Building.tags attribute defined by Tag.building backref

# TODO: Remove legacy Category?
class Category(db.Model):
    """
    DB model representing a category associated with a building
    """
    __tablename__ = 'categories'

    cat_id = db.Column('cat_id', Integer, primary_key=True, autoincrement=True)
    # TODO: DB table doesn't but should have foriegn key- lying here to SQL Alchemy
    b_id = db.Column('b_id', Text, ForeignKey("buildings.b_id"), nullable=False)
    cat_name = db.Column('cat_name', Text, nullable=False)

    # TODO: update when the table has a proper foriegn key constraint
    # building relationship - this is a more complex as there is not a proper foreign key and the b_id column types differ
    buildings = db.relationship('Building', backref=('categories'), primaryjoin=cast(remote(Building.b_id), Text) == foreign(b_id))


class Tag(db.Model):
    """
    DB model representing a tag associated with a building
    """
    __tablename__ = 'tags'
    __table_args__ = (UniqueConstraint('b_id', 'tag_name'),)

    tag_id = db.Column('tag_id', Integer, primary_key=True, autoincrement=True)
    # TODO: DB table doesn't but should have foriegn key- lying here to SQL Alchemy
    b_id = db.Column('b_id', Text, ForeignKey("buildings.b_id"), nullable=False)
    tag_name = db.Column('tag_name', Text, nullable=False)
    gtuser = db.Column('gtuser', Text, nullable=False)
    auth = db.Column('auth', Integer, default=0)
    times_tag = db.Column('times_tag', Integer, default=1, nullable=False)
    flag_users = db.Column('flag_users', Text, nullable=True)
    times_flagged = db.Column('times_flagged', Integer, default=0, nullable=False)

    # TODO: update when the table has a proper foreign key constraint
    # building relationship - this is a more complex as there is not a proper foreign key and the b_id column types differ
    building = db.relationship('Building', backref=('tags'), primaryjoin=cast(remote(Building.b_id), Text) == foreign(b_id))