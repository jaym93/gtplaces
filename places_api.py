import sys
import flask
from sqlalchemy import create_engine, MetaData, Table, Column, Index, UniqueConstraint
from sqlalchemy import Integer, Float, String, Text
from sqlalchemy.sql import select, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError
from flasgger import Swagger
from flask import request
from flask_cas import CAS, login_required
import conf  # all configurations are stored here, change individually for development and release configurations.

# Import the right configuration from conf.py, based on if it is the development environment or release environment
# Run 'python3 places_api.py release' for deployment to release, 'python3 places_api.py dev' or 'python3 places_api.py' will deploy to development environment
if __name__ == '__main__':
    env = sys.argv[1] if len(sys.argv) > 2 else 'dev'  # always fall back to dev environment
    config = conf.get_conf(env)

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": config['SWAGGER_Title'],
        "description": config['SWAGGER_Description'],
        "contact": {
            "responsibleOrganization": "GT-RNOC",
            "responsibleDeveloper": "RNOC Lab Staff",
            "email": "rnoc-lab-staff@lists.gatech.edu",
            "url": "http://rnoc.gatech.edu/"
        },
        # "termsOfService": "http://me.com/terms",
        "version": "2.0"
    },
    "host": config['SWAGGER_Host'],  # Places API is hosted here
    "basePath": "/",  # base bash for blueprint registration
    "schemes": ["http", "https"],
}

# Flask stuff
app = flask.Flask(__name__)
cas = CAS(app)
swag = Swagger(app, template=swagger_template)
app.config['CAS_SERVER'] = config['CAS_Server']
app.config['CAS_VALIDATE_ROUTE'] = config['CAS_ValRoute']
app.config['SECRET_KEY'] = config['CAS_Secret']  # set a random key, otherwise the authentication will throw errors
app.config['SESSION_TYPE'] = 'filesystem'
app.config['CAS_AFTER_LOGIN'] =''

# SQLAlchemy stuff
db = create_engine(config['SQLA_ConnString'] + config['SQLA_DbName'], echo=config['SQLA_Echo'])
Base = declarative_base()
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

def get_categories(b_id):
    """
    Get all the categories a building belongs to
    """
    query = select([categories.c.cat_name], categories.c.b_id ==  b_id).distinct()
    results = db.execute(query).fetchall()
    categories_ret = []
    for res in results:
        categories_ret.append(res[0])
    return categories_ret

def get_tags(b_id):
    """
    Get all the tags a building is associated with
    """
    query = select([tags.c.tag_name], tags.c.b_id == b_id).distinct()
    results = db.execute(query).fetchall()
    tags_ret = []
    for res in results:
        tags_ret.append(res[0])
    return tags_ret

def res_to_json(row):
    """
    Encode the result of a place-related SQL query to JSON
    """
    output = {
        "b_id": row[0],
        "name": row[2],
        "category": get_categories(row[0]),
        "address": row[3],
        "address2": row[4],
        "zipcode": row[5],
        "image_url": row[6],
        "website_url": row[7],
        "latitude": row[8],
        "longitude": row[9],
        "shape_coordinates": row[10],
        "phone_num": row[11],
        "tags": get_tags(row[0])
    }
    return(output)

@app.route("/checkuser",methods=['GET'])
@login_required
def index():
    """
    Check if user is logged in, or ask user to log in
    Simply test to see if the user is authenticated, and return their login name
    ---
    tags:
        - user
    produces:
	- application/json
    responses:
        200:
	    description: User is logged in
            schema:
                type: object
                properties:
                    username:
                         type: string
                         description: username of the user currently logged in
                         required: true
        403:
            description: Unable to authenticate
            schema:
                type: object
                properties:
                    error:
                        type: string
                        description: unable to authenticate
                        required: true
    """
    try:
        return flask.jsonify({"username":cas.username}), 200
    except:
        return flask.jsonify({"error":"Unable to authenticate"}), 403

@app.route("/gtplaces/buildings", methods=['GET'])
def getAll():
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
    query = buildings.select()
    results = db.execute(query)
    response = []
    for result in results:
        response.append(res_to_json(result))
    return flask.jsonify(response)

@app.route("/gtplaces/buildings_id/<b_id>", methods=['GET'])
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
    query = select([buildings], buildings.c.b_id == b_id)
    results = db.execute(query).fetchall()
    response = []
    for result in results:
        response = res_to_json(result)
    return flask.jsonify(response)

@app.route("/gtplaces/buildings/<name>", methods=['GET'])
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
    query = select([buildings], buildings.c.name.like('%' + name + '%'))
    results = db.execute(query).fetchall()
    response = []
    for result in results:
        response.append(res_to_json(result))
    return flask.jsonify(response)

@app.route("/gtplaces/categories", methods=['GET'])
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
    response = []
    query = select([categories.c.cat_name]).distinct()
    results = db.execute(query).fetchall()
    for result in results:
        response.append(result[0])
    return flask.jsonify(response)

@app.route("/gtplaces/categories", methods=['POST'])
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
    response = []
    category = request.form["category"]
    query = select([buildings, categories], and_(categories.c.cat_name == category, categories.c.b_id == buildings.c.b_id))
    results = db.execute(query).fetchall()
    response = []
    for result in results:
        response.append(res_to_json(result))
    return flask.jsonify(response)

@app.route("/gtplaces/tags", methods=['GET'])
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
    response = []
    query = select([tags])
    results = db.execute(query)
    for result in results:
        response.append({
            "tag_id": result[0],
            "b_id": result[1],
            "tag_name": result[2],
            "gtuser": result[3],
            "auth": result[4],
            "times_tag": result[5],
            "flag_users": result[6],
            "times_flagged": result[7]
        })
    return flask.jsonify(response)

@app.route("/gtplaces/tags", methods=['POST'])
@login_required
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
    bid = request.form['b_id']
    tag = request.form['tag']
    tag = "'"+tag+"'" # for some weird reason, each tag in the database is surrounded with single quotes
    if bid=="" or tag=="":
        return flask.jsonify({"error": "Building ID or Tag Name cannot be empty!"}), 400
    try:  # SQLAlchemy does not have a ON DUPLICATE UPDATE method, this is the best workaround I found
        query = tags.insert().values(b_id=bid, tag_name=tag, gtuser=cas.username, auth=0, times_tag=1, flag_users='', times_flagged=0)
        db.execute(query)
    except IntegrityError:
        query = tags.update(and_(tags.c.tag_name == tag, tags.c.b_id == bid), values={tags.c.times_tag: tags.c.times_tag+1})
        db.execute(query)
    return flask.jsonify({"status": "tag inserted"}), 201

@app.route("/gtplaces/tags/<name>", methods=['GET'])
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
    response = []
    query = select([tags.c.tag_id, tags.c.b_id, tags.c.tag_name, tags.c.gtuser, tags.c.auth, tags.c.times_tag, tags.c.flag_users, tags.c.times_flagged], and_(tags.c.tag_name.like('%' + name + '%'), tags.c.b_id == buildings.c.b_id))
    results = db.execute(query)
    for result in results:
        response.append({
            "tag_id": result[0],
            "b_id": result[1],
            "tag_name": result[2],
            "gtuser": result[3],
            "auth": result[4],
            "times_tag": result[5],
            "flag_users": result[6],
            "times_flagged": result[7]
        })
    return flask.jsonify(response)

@app.route("/gtplaces/flag", methods=['POST'])
@login_required
def flagTag():
    """
    Flag a certain tag as being incorrect
    Send 'tag_id' (Tag ID) as form data to flag an existing tag in the database.
    If Tag ID does not exist, your flag will be ignored.
    *Using this method requires you to be logged in via CAS.*
    ---
    tags:
        - tags
    consumes:
        - application/x-www-form-urlencoded
    parameters:
        - name: tag_id
          in: formData
          description: Tag ID to flag (example, 30)
          required: true
          type: string
    produces:
        - application/json
    responses:
        201:
            description: Tag flagged
        400:
            description: Bad request, Tag ID ('tag_id') missing in POST body
    """
    tag_id = request.form['tag_id']  # Only flag an existing tag, changing this from the legacy implementation where you could tag by building ID
    if tag_id == "":
        return flask.jsonify({"error": "Tag ID is required"}), 400
    query = tags.update(tags.c.tag_id == tag_id, values={tags.c.flag_users: tags.c.flag_users+cas.username+',', tags.c.times_flagged: tags.c.times_flagged+1})
    db.execute(query)
    return flask.jsonify({"status": "tag flagged"}), 201

app.run(host=config['FLASK_Host'], port=config['FLASK_Port'], debug=config['FLASK_Debug'])

