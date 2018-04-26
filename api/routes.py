"""
Places API route / endpoint implementations

Uses Flask Blueprints as explained here:
http://flask.pocoo.org/docs/0.12/blueprints/#blueprints
"""
from http import HTTPStatus

import flask
from flask import request, Blueprint
from flask_cas import login_required

from api.errors import NotFoundException, BadRequestException
from api.extensions import cas, db, cors
from api.models import Building, Tag, Category
from api.schema import buildings_schema, building_schema, tags_schema, tag_schema

api = Blueprint('gtplaces', __name__)


@api.route("/buildings/", methods=['GET'])
def getBuildings():
    """
    Returns list of all buildings with their information
    Returns list of all buildings with building id, name, address, phone, website, latitude, longtitude, map shape coordinates, image url and tags.
    ---
    tags:
        - buildings
    produces:
        - application/json
    responses:
        200:
            description: An array of building information
            schema:
                type: array
                items:
                    type: object
                    properties:
                      b_id:
                        type: string
                        description: ID of the building
                        required: true
                      name:
                        type: string
                        description: Name of the building
                        required: true
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
                            type:string
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
                      latitute:
                        type: string
                        description: Latitute of the building
                      longitute:
                        type: string
                        description: Longitute of the building
                      shape_coordinates:
                        type: string
                        description: Map poly-coordinates of the building
                      tag_list:
                        type: array
                        items:
                          type: string
                        description: Tags of the building
    """
    buildings = Building.query.all()
    return buildings_schema.jsonify(buildings)


@api.route("/buildings_id/<b_id>/", methods=['GET'])
def getById(b_id):
    """
    Search building by ID
    Given building ID, returns the building with building id, name, address, phone, website, latitude, longtitude, map shape coordinates, image url and tags.
    ---
    tags:
        - buildings
    produces:
        - application/json
    parameters:
        - name: b_id
          in: path
          description: ID of the building.
          required: true
          type: string
          default: 50
    responses:
        200:
            description: An array of building information
            schema:
                type: array
                items:
                    type: object
                    properties:
                      b_id:
                        type: string
                        description: ID of the building
                        required: true
                      name:
                        type: string
                        description: Name of the building
                        required: true
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
                            type:string
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
                      latitute:
                        type: string
                        description: Latitute of the building
                      longitute:
                        type: string
                        description: Longitute of the building
                      shape_coordinates:
                        type: string
                        description: Map poly-coordinates of the building
                      tag_list:
                        type: array
                        items:
                          type: string
                        description: Tags of the building
    """
    building = Building.query.filter_by(b_id=b_id).first()
    if not building:
        raise NotFoundException()
    return building_schema.jsonify(building)


@api.route("/buildings/<name>/", methods=['GET'])
def getByName(name):
    """
    Search building by name
    Given a part of a building name, returns the building with building id, name, address, phone, website, latitude, longtitude, map shape coordinates, image url and tags.
    ---
    tags:
        - buildings
    parameters:
        - name: name
          in: path
          description: Name of the building (partial names are okay).
          required: true
          type: string
          default: College of Computing
    produces:
        - application/json
    responses:
        200:
            description: An array of building information
            schema:
                type: array
                items:
                    type: object
                    properties:
                      b_id:
                        type: string
                        description: ID of the building
                        required: true
                      name:
                        type: string
                        description: Name of the building
                        required: true
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
                            type:string
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
                      latitute:
                        type: string
                        description: Latitute of the building
                      longitute:
                        type: string
                        description: Longitute of the building
                      shape_coordinates:
                        type: string
                        description: Map poly-coordinates of the building
                      tag_list:
                        type: array
                        items:
                          type: string
                        description: Tags of the building
    """
    buildings = Building.query.filter_by(name=name)
    return buildings_schema.jsonify(buildings)


@api.route("/categories/", methods=['GET'])
def getCategories():
    """
    Return lists of all categories
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


@api.route("/categories/", methods=['POST'])
def postCategories():
    """
    List all buildings in a certain category
    Send 'category' in body with the category name to get all the buildings and associated information.
    Categories are one of "University", "Housing" or "Greek", and is being preserved for legacy reasons.
    ---
    tags:
        - categories
    deprecated: true
    consumes:
        - application/x-www-form-urlencoded
    parameters:
        - name: category
          in: formData
          description: Category name. Current values are University, Housing and Greek.
          required: true
          type: string
          default: University
    produces:
        - application/json
    responses:
        200:
            description: List of all gtplaces categories
            schema:
                type: array
                items:
                    type: object
                    properties:
                      b_id:
                        type: string
                        description: ID of the building
                        required: true
                      name:
                        type: string
                        description: Name of the building
                        required: true
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
                            type:string
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
                      latitute:
                        type: string
                        description: Latitute of the building
                      longitute:
                        type: string
                        description: Longitute of the building
                      shape_coordinates:
                        type: string
                        description: Map poly-coordinates of the building
                      tag_list:
                        type: array
                        items:
                          type: string
                        description: Tags of the building
    """
    category = request.form['category']
    buildings = Building.query.filter(Building.categories.any(cat_name=category))
    return buildings_schema.jsonify(buildings)


@api.route("/tags/", methods=['GET'])
def getTags():
    """
    Return lists of all tags
    Lists all the tags in the GTPlaces database, with the associated information (Tag ID, Building ID it is associated with, User who created it, number of times it has been tagged or flagged).
    Tags let users search by substrings associated with abbreviations, acronyms, aliases or sometimes even events inside a building. For example, Office of International Education is inside the Savant building, and Tags exists so there can be a mapping from "OIE" to "Savant building" so it appears in the search results.
    ---
    tags:
        - tags
    produces:
        - application/json
    responses:
        200:
            description: List of all gtplaces tags
            schema:
                type: array
                items:
                    type: object
                    properties:
                      tag_id:
                        type: string
                        required: true
                        description: ID of the tag (autoincrement)
                      b_id:
                        type: string
                        required: true
                        description: ID of the building the tag is associated with
                      tag_name:
                        type: string
                        description: Tag label
                      gtuser:
                        type: string
                        description: User who created the tag (First user, in case of multiple times tagged)
                      auth:
                        type: string
                        description: (only here for compatibility reasons, not used)
                      times_tag:
                        type: string
                        description: Number of times this building has been tagged (possibly by different users)
                      flag_users:
                        type: string
                        description: Users who have flagged this tag (First user, in case of multiple times tagged)
                      times_flagged:
                        type: string
                        description: Number of times this tag has been flagged
    """
    tags = Tag.query.all()
    return tags_schema.jsonify(tags)

# TODO: secure
@api.route("/tags/", methods=['POST'])
#@login_required
def addTag():
    """
    Add a tag
    Send 'b_id' (building ID), 'tag' (Tag Name) in POST body to add to the database.
    Tags let users create searchable substrings associated with abbreviations, acronyms, aliases or sometimes even events inside a building. For example, Office of International Education is inside the Savant building, and Tags exists so there can be a mapping from "OIE" to "Savant building" so it appears in the search results.
    *Using this method requires you to be logged in via CAS.*
    ---
    tags:
        - tags
    consumes:
        - application/x-www-form-urlencoded
    parameters:
        - name: b_id
          in: formData
          description: Id of the building
          required: true
          type: string
        - name: tag
          in: formData
          description: Name of the tag that you want to add to the building
          required: true
          type: string
    produces:
        - application/json
    responses:
        201:
            description: Tag inserted
        400:
            description: Bad request, Building ID ('b_id') or Tag Name ('tag') missing in POST body
    """
    b_id = request.form['b_id']
    tag_name = request.form['tag']
    if not b_id or not tag_name:
        raise BadRequestException(message="'b_id' and 'tag' required")

    tag = Tag.query.filter_by(b_id=b_id, tag_name=tag_name).first()
    if tag:
        tag.times_tag = Tag.times_tag + 1
    else:
        # TODO: get user from auth token
        gtuser = 'anonymous'
        tag = Tag(b_id=b_id, tag_name=tag_name, gtuser=gtuser)
        db.session.add(tag)
    db.session.commit()

    return tag_schema.jsonify(tag), HTTPStatus.CREATED


@api.route("/tags/<name>/", methods=['GET'])
def getByTagName(name):
    """
    Returns info about a particular tag
    Given the tag name, the API returns all the information (Tag ID, Building ID it is associated with, User who created it, number of times it has been tagged or flagged) associated with that tag name.
    ---
    tags:
        - tags
    parameters:
        - name: name
          in: path
          description: Name of the tag.
          required: true
          type: string
          default: coc
    produces:
        - application/json
    responses:
        200:
            description: List of all places associated with a certain tag
            schema:
                type: array
                items:
                    type: object
                    properties:
                      tag_id:
                        type: string
                        required: true
                        description: ID of the tag (autoincrement)
                      b_id:
                        type: string
                        required: true
                        description: ID of the building the tag is associated with
                      tag_name:
                        type: string
                        description: Tag label
                      gtuser:
                        type: string
                        description: User who created the tag (First user, in case of multiple times tagged)
                      auth:
                        type: string
                        description: (only here for compatibility reasons, not used)
                      times_tag:
                        type: string
                        description: Number of times this building has been tagged (possibly by different users)
                      flag_users:
                        type: string
                        description: Users who have flagged this tag (First user, in case of multiple times tagged)
                      times_flagged:
                        type: string
                        description: Number of times this tag has been flagged
    """
    tag = Tag.query.filter_by(tag_name=name).first()
    return tag_schema.jsonify(tag)

# TODO: secure
@api.route("/flag/", methods=['POST'])
#@login_required
def flagTag():
    """
    Flag a certain tag as being incorrect
    Send 'tag_name' as form data to flag an existing tag in the database.
    If Tag ID does not exist, your flag will be ignored.
    *Using this method requires you to be logged in via CAS.*
    ---
    tags:
        - tags
    consumes:
        - application/x-www-form-urlencoded
    parameters:
        - name: tag_name
          in: formData
          description: Tag name to flag (example, 'recreation')
          required: true
          type: string
    produces:
        - application/json
    responses:
        201:
            description: Tag flagged
        400:
            description: Bad request, `tag_name` missing in POST body
    """
    # Only flag an existing tag, changing this from the legacy implementation where you could tag by building ID (Jayanth)
    tag_name = request.form['tag_name']
    if not tag_name:
        raise BadRequestException(message="'tag' required")

    tag = Tag.query.filter_by(tag_name=tag_name).first()
    if not tag:
        raise NotFoundException()
    else:
        # TODO: get user from auth token
        gtuser = 'anonymous'
        # only flag the first once per user
        if not (gtuser in tag.flag_users.split(',')):
            tag.times_flagged = Tag.times_flagged + 1
            tag.flag_users = Tag.flag_users + gtuser + ','
            db.session.commit()
        return tag_schema.jsonify(tag), HTTPStatus.CREATED


