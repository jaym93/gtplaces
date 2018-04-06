"""
Schema for JSON exposed by the API.

See Marshmallow documentation:
https://flask-marshmallow.readthedocs.io/en/latest/
http://marshmallow.readthedocs.io/en/latest/
"""
from api.extensions import ma


class TagSchema(ma.Schema):
    """
    JSON schema for a building tag
    """
    class Meta:
        # JSON fields - type will be inferred
        # TODO: not exposing 'app_id', 'auth' fields
        fields = ('tag_id', 'b_id', 'tag_name', 'gtuser', 'times_tag', 'flag_users', 'times_flagged')


class CategorySchema(ma.Schema):
    """
    JSON schema for a building category
    """
    class Meta:
        # JSON fields - type will be inferred
        fields = ('cat_name',)


class BuildingSchema(ma.Schema):
    """
    JSON schema for a building
    """
    class Meta:
        # JSON fields - type will be inferred
        # TODO: not exposing 'app_id', however this is in the database
        fields = ('b_id', 'name', 'address', 'address2', 'zipcode', 'image_url', 'website_url', 'latitude', 'longitude',
                  'shape_coordinates', 'phone_num', 'tags', 'categories')
    # 'address2' field maps to the DB model attribute 'city', which must explicitly defined w/ attribute mapping
    address2 = ma.String(attribute='city')

    # include lists of only the tag and category names
    tags = ma.Nested(TagSchema, only='tag_name', many=True)
    categories = ma.Nested(CategorySchema, only='cat_name', many=True)


building_schema = BuildingSchema()
buildings_schema = BuildingSchema(many=True)

tag_schema = TagSchema()
tags_schema = TagSchema(many=True)
