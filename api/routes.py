"""
Places API route / endpoint implementations

Uses Flask Blueprints as explained here:
http://flask.pocoo.org/docs/0.12/blueprints/#blueprints
"""
from http import HTTPStatus

import flask
from flask import request, Blueprint
from marshmallow import ValidationError

from api.errors import NotFoundException, BadRequestException
from api.extensions import db #, wso2auth
from api.models import Building, Tag, Category
from api.schema import buildings_schema, building_schema, tags_schema, tag_schema

api = Blueprint('gtplaces', __name__)


@api.route("/buildings/", methods=['GET'])
def getBuildings():
    """
    Returns all buildings with optional filtering
    Returns list of all buildings with building id, name, address, phone, website, latitude, longtitude, map shape coordinates, image url and tags.
    Optionally, return only buildings matching a given name, category or tag.
    ---
    tags:
        - buildings
    produces:
        - application/json
    parameters:
        - name: name
          in: query
          description: Filter results by name. May use % character as wild card.
          required: false
          type: string
        - name: category
          in: query
          description: Filter results by category.
          required: false
          type: string
        - name: tag
          in: query
          description: Filter results by tag.
          required: false
          type: string
    responses:
        200:
            description: Collection of building information
            schema:
                type: array
                items:
                    $ref: '#/definitions/Building'
    """
    name = request.args.get('name')
    category = request.args.get('category')
    tag = request.args.get('tag')

    query = Building.query
    query = query.filter(Building.name.ilike(name)) if name else query
    query = query.filter(Building.categories.any(cat_name=category)) if category else query
    query = query.filter(Building.tags.any(tag_name=tag)) if tag else query

    return buildings_schema.jsonify(query.all())


@api.route("/buildings/<b_id>", methods=['GET'])
def getBuilding(b_id):
    """
    Gets building with the given ID
    Given building ID, returns the building with building id, name, address, phone, website, latitude, longtitude, map shape coordinates, image url and tags.
    ---
    tags:
        - buildings
    definitions:
        Building:
            type: array
            items:
                type: object
                properties:
                  b_id:
                    type: string
                    description: ID of the building
                  name:
                    type: string
                    description: Name of the building
                  address:
                    type: string
                    description: Address of the building
                  address2:
                    type: string
                    description: City and state
                  zipcode:
                    type: string
                    description: Zipcode of the building
                  category:
                    type: array
                    items:
                      type: string
                    description: The categories the building belongs to
                  image_url:
                    type: string
                    description: Image of the building
                  website_url:
                    type: string
                    description: Website of the building
                  phone_num:
                    type: string
                    description: Phone number of the building
                  latitude:
                    type: string
                    description: Latitude of the building
                  longitude:
                    type: string
                    description: Longitude of the building
                  shape_coordinates:
                    type: string
                    description: Map poly-coordinates of the building
                  tag_list:
                    type: array
                    items:
                      type: string
                    description: Tags of the building
                required:
                  - b_id
                  - name
    produces:
        - application/json
    parameters:
        - name: b_id
          in: path
          description: ID of the building.
          required: true
          type: string
    responses:
        200:
            description: Building information
            schema:
                $ref: '#/definitions/Building'
    """
    building = Building.query.filter_by(b_id=b_id).first()
    if not building:
        raise NotFoundException()
    return building_schema.jsonify(building)


@api.route("/categories/", methods=['GET'])
def getCategories():
    """
    Return list of all categories
    Lists all the categories in the GTPlaces database
    Categories are one of "University", "Housing" or "Greek", and is being preserved for legacy reasons.
    ---
    tags:
        - categories
    deprecated: true
    produces:
        - application/json
    responses:
        200:
            description: List of all gtplaces categories
            schema:
                type: array
                items:
                  type: string
                description: List of all categories
    """
    categories = [r.cat_name for r in db.session.query(Category.cat_name).distinct()]
    return flask.jsonify(categories)


@api.route("/tags/", methods=['GET'])
def getTags():
    """
    Return list of all tags
    Lists all building tags, with the associated metadata.
    Tags provide additional keywords to to improve building searches.
    ---
    tags:
        - tags
    definitions:
        TagWithMetadata:
            type: object
            properties:
              b_id:
                type: string
                description: ID of the building with which this the tag is associated
              tag_name:
                type: string
                description: Name of the tag
              gtuser:
                type: string
                description: User who created the tag
              auth:
                type: string
                description: Present for legacy compatibility, not used.
              times_tag:
                type: string
                description: Number of times the tag has been applied to this building
              flag_users:
                type: string
                description: Users who have flagged this tag as incorrect or inappropriate
              times_flagged:
                type: string
                description: Number of times this tag has been flagged
    produces:
        - application/json
    responses:
        200:
            description: List of all tags with associated metadata
            schema:
                type: array
                items:
                    $ref: '#/definitions/TagWithMetadata'

    """
    tags = Tag.query.all()
    return tags_schema.jsonify(tags)


# DISABLING ENDPOINTS that allow writes due to removal of authentication.

# @api.route("/buildings/<b_id>/tags/", methods=['POST'])
# @wso2auth.application_gt_user_required()
# def addBuildingTag(b_id):
#     """
#     Add a tag to a building.
#     Tags let users create searchable substrings associated with abbreviations, acronyms, aliases or sometimes even events inside a building. For example, Office of International Education is inside the Savant building, and Tags exists so there can be a mapping from "OIE" to "Savant building" so it appears in the search results.
#     *Login required.*
#     ---
#     tags:
#         - tags
#     consumes:
#         - application/json
#     parameters:
#         - name: b_id
#           in: path
#           description: ID of the building
#           required: true
#           type: string
#         - in: body
#           name: body
#           description: Tag
#           required: true
#           schema:
#             type: object
#             properties:
#               tag_name:
#                 type: string
#                 description: Name of the tag
#     produces:
#         - application/json
#     responses:
#         201:
#             description: Created tag with associated metadata
#             schema:
#                 $ref: '#/definitions/TagWithMetadata'
#         400:
#             description: Bad request
#     """

#     try:
#         request_body = tag_schema.load(request.get_json())
#     except ValidationError as e:
#         # TODO: update error JSON to include details of field errors, reported as dictionary by ValidationError
#         raise BadRequestException('Invalid request body: ' + str(e.messages))

#     building_exists = Building.query.filter_by(b_id=b_id).count() == 1
#     if not building_exists:
#         raise NotFoundException()

#     tag = Tag.query.filter_by(b_id=b_id, tag_name=request_body['tag_name']).first()
#     if tag:
#         tag.times_tag = Tag.times_tag + 1
#     else:
#         gtuser = wso2auth.username
#         tag = Tag(b_id=b_id, tag_name=request_body['tag_name'], gtuser=gtuser)
#         db.session.add(tag)
#     db.session.commit()

#     return tag_schema.jsonify(tag), HTTPStatus.CREATED


@api.route("/buildings/<b_id>/tags/", methods=['GET'])
def getBuildingTags(b_id):
    """
    Returns all tags for the given building
    Returns all tags with their metadata for the given building.
    ---
    tags:
        - tags
    parameters:
        - name: b_id
          in: path
          description: ID of the building
          required: true
          type: string
    produces:
        - application/json
    responses:
        200:
            description: List of tags with associated metadata for the building
            schema:
                type: array
                items:
                    $ref: '#/definitions/TagWithMetadata'
    """
    building_exisits = Building.query.filter_by(b_id=b_id).count() == 1
    if not building_exisits:
        raise NotFoundException()
    tags = Tag.query.filter_by(b_id=b_id)
    return tags_schema.jsonify(tags)


@api.route("/buildings/<b_id>/tags/<tag_name>", methods=['GET'])
def getBuildingTag(b_id, tag_name):
    """
    Returns the specific building tag with metadata
    Returns the tag with metadata for the given building tag.
    ---
    tags:
        - tags
    parameters:
        - name: b_id
          in: path
          description: ID of the building
          required: true
          type: string
        - name: tag_name
          in: path
          description: Tag name
          required: true
          type: string
    produces:
        - application/json
    responses:
        200:
            description: Tag with associated metadata
            schema:
                $ref: '#/definitions/TagWithMetadata'
    """
    tag = Tag.query.filter_by(b_id=b_id, tag_name=tag_name).first()
    if not tag:
        raise NotFoundException()
    return tag_schema.jsonify(tag)


# DISABLING ENDPOINTS that allow writes due to removal of authentication.

# @api.route("/buildings/<b_id>/tags/<tag_name>/flag", methods=['POST'])
# @wso2auth.application_gt_user_required()
# def flagBuildingTag(b_id, tag_name):
#     """
#     Flag a building tag as being incorrect or inappropriate
#     Flag a building tag as being incorrect or inappropriate.  POST requires no body.
#     *Login required.*
#     ---
#     tags:
#         - tags
#     parameters:
#         - name: b_id
#           in: path
#           description: ID of the building
#           required: true
#           type: string
#         - name: tag_name
#           in: path
#           description: Tag to flag
#           required: true
#           type: string
#     produces:
#         - application/json
#     responses:
#         201:
#             description: Flagged tag with associated metadata
#             schema:
#                 $ref: '#/definitions/TagWithMetadata'
#     """
#     tag = Tag.query.filter_by(b_id=b_id, tag_name=tag_name).first()
#     if not tag:
#         raise NotFoundException()
#     else:
#         gtuser = wso2auth.username
#         # only flag the first once per user
#         if not (gtuser in tag.flag_users.split(',')):
#             tag.times_flagged = Tag.times_flagged + 1
#             tag.flag_users = Tag.flag_users + gtuser + ','
#             db.session.commit()
#         return tag_schema.jsonify(tag), HTTPStatus.CREATED


