import json
import pymysql
import flask
from flasgger import Swagger, MK_SANITIZER
from flask import request
from flask_cas import CAS, login_required
from flask_cas import login, logout
import os

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Places API",
        "description": "This API will allow you to access the information of the places at Georgia Tech. It can be used to find out information about the offices and the buildings such as their names, addresses, phone numbers, images, categories and GPS coordinates.",
        "contact": {
            "responsibleOrganization": "GT-RNOC",
            "responsibleDeveloper": "Jayanth Mohana Krishna",
            "email": "jayanth6@gatech.edu",
            "url": "http://rnoc.gatech.edu/",
        },
        # "termsOfService": "http://me.com/terms",
        "version": "2.0"
    },
    "host": "dockertest.rnoc.gatech.edu:5000",  # Places API is hosted here
    "basePath": "/",  # base bash for blueprint registration
    "schemes": ["http", "https"],

}

app = flask.Flask(__name__)
cas = CAS(app)
swag = Swagger(app, template=swagger_template, sanitizer=MK_SANITIZER)
app.config['CAS_SERVER'] = 'https://login.gatech.edu/cas'
app.config['CAS_VALIDATE_ROUTE'] = '/serviceValidate'
app.config['SECRET_KEY'] = '6d4e24b1bbaec5f6f7ac35878920b8ebdfdf71bc53521f31bc4ec47885de610d' #set a random key, otherwise the authentication will throw errors
app.config['SESSION_TYPE'] = 'filesystem'
app.config['CAS_AFTER_LOGIN'] =''

conn = pymysql.connect(host='db0.rnoc.gatech.edu', port=3306, user=os.environ['DB_USERNAME'], passwd=os.environ['DB_PASSWORD'], db='CORE_gtplaces')
cur = conn.cursor()

@app.errorhandler(pymysql.DatabaseError)
def dbconnectionhandler(error):
    return flask.jsonify({"error":"Database connection failed"}), 500

def get_categories(b_id):
    """
    Get all the categories a building belongs to
    """
    query = "select distinct cat_name from categories where b_id='"+b_id+"'"
    results = cur.execute(query)
    results = cur.fetchall()
    categories = []
    for res in results:
        categories.append(res[0])
    return categories

def get_tags(b_id):
    """
    Get all the tags a building is associated with
    """
    query = "select distinct tag_name from tags where b_id='"+b_id+"'"
    results = cur.execute(query)
    results = cur.fetchall()
    categories = []
    for res in results:
        categories.append(res[0])
    return categories

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

@app.route("/",methods=['GET'])
@login_required
def index():
    """
    Simply test to see if the user is authenticated, and return their login name
    """
    username = cas.username
    return "Logged in as: " + username

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
    query = "select * from buildings"
    cur.execute(query)
    results = cur.fetchall()
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
    query = "select * from buildings where b_id = '"+b_id+"'"
    cur.execute(query)
    results = cur.fetchall()
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
    query = "select * from buildings where name like '%" + name + "%'"
    cur.execute(query)
    results = cur.fetchall()
    response = []
    for result in results:
        response.append(res_to_json(result))
    return flask.jsonify(response)

@app.route("/gtplaces/categories", methods=['GET'])
def getCategories():
    """
    Return lists of all categories
    Lists all the categories in the GTPlaces database.
    _Categories are one of "University", "Housing" or "Greek", and is being preserved for legacy reasons._
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
    query = "select distinct cat_name from categories"
    cur.execute(query)
    results = cur.fetchall()
    for result in results:
        response.append(result[0])
    return flask.jsonify(response)

@app.route("/gtplaces/categories", methods=['POST'])
def postCategories():
    """
    List all buildings in a certain category
    Send 'category' in body with the category name to get all the buildings and associated information.
    _Categories are one of "University", "Housing" or "Greek", and is being preserved for legacy reasons._
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
    query = "select * from buildings b, categories c where c.cat_name = '"+category+"' and c.b_id = b.b_id"
    cur.execute(query)
    results = cur.fetchall()
    response = []
    for result in results:
        response.append(res_to_json(result))
    return flask.jsonify(response)

@app.route("/gtplaces/tags", methods=['GET'])
def getTags():
    """
    Return lists of all tags
    Lists all the tags in the GTPlaces database, with the associated information (Tag ID, Building ID it is associated with, User who created it, number of times it has been tagged or flagged).
    _Tags let users search by substrings associated with abbreviations, acronyms, aliases or sometimes even events inside a building. For example, Office of International Education is inside the Savant building, and Tags exists so there can be a mapping from "OIE" to "Savant building" so it appears in the search results._
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
    query = "select * from tags"
    cur.execute(query)
    results = cur.fetchall()
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
    if (bid=="" or tag==""):
        return flask.jsonify({"error": "Building ID or Tag Name cannot be empty!"}), 400
    query = "insert into tags (b_id,tag_name,gtuser,auth,times_tag,flag_users,times_flagged) values ('"+bid+"','"+tag+"','"+cas.username+"',0,1,'',0) ON DUPLICATE KEY UPDATE times_tag=times_tag+1"
    cur.execute(query)
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
    query = "select t.tag_id, t.b_id, t.tag_name, t.gtuser, t.auth, t.times_tag, t.flag_users, t.times_flagged from buildings b, tags t where tag_name like '%" + name + "%' and b.b_id = t.b_id"
    cur.execute(query)
    results = cur.fetchall()
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
    tag_id = request.form['tag_id'] # Only flag an existing tag, changing this from the legacy implementation where you could tag by building ID
    if tag_id == "":
        return flask.jsonify({"error": "Tag ID is required"}), 400
    query = "update tags set flag_users = concat(flag_users, '" +cas.username+ ",'), times_flagged=times_flagged+1 where tag_id="+ tag_id
    cur.execute(query)
    return flask.jsonify({"status": "tag flagged"}), 201

app.run(host='0.0.0.0', port=5000, debug=True)