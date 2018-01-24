import json
import pymysql
import flask
from flask import request
from flask_cas import CAS, login_required
from flask.ext.cas import login, logout
import os

app = flask.Flask(__name__)
cas = CAS(app)
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
    query = "select distinct cat_name from categories where b_id='"+b_id+"'"
    results=cur.execute(query)
    results = cur.fetchall()
    categories = []
    for res in results:
        categories.append(res[0])
    return categories

def get_tags(b_id):
    query = "select distinct tag_name from tags where b_id='"+b_id+"'"
    results=cur.execute(query)
    results = cur.fetchall()
    categories = []
    for res in results:
        categories.append(res[0])
    return categories

def res_to_json(row):
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
    username = cas.username
    return "Logged in as: " + username

@app.route("/gtplaces/buildings", methods=['GET'])
def getAll():
    query = "select * from buildings"
    cur.execute(query)
    results = cur.fetchall()
    response = []
    for result in results:
        response.append(res_to_json(result))
    return flask.jsonify(response)

@app.route("/gtplaces/buildings_id/<b_id>", methods=['GET'])
def getById(b_id):
    query = "select * from buildings where b_id = '"+b_id+"'"
    cur.execute(query)
    results = cur.fetchall()
    response = []
    for result in results:
        response = res_to_json(result)
    return flask.jsonify(response)

@app.route("/gtplaces/buildings/<name>", methods=['GET'])
def getByName(name):
    query = "select * from buildings where name like '%" + name + "%'"
    cur.execute(query)
    results = cur.fetchall()
    response = []
    for result in results:
        response.append(res_to_json(result))
    return flask.jsonify(response)

@app.route("/gtplaces/categories", methods=['GET','POST'])
def getCategories():
    response = []
    if(request.method=='GET'):
        query = "select distinct cat_name from categories"
        cur.execute(query)
        results = cur.fetchall()
        for result in results:
            response.append(result[0])
    elif(request.method=='POST'):
        category = request.get_json()['category']
        query = "select * from buildings b, categories c where c.cat_name = '"+category+"' and c.b_id = b.b_id"
        cur.execute(query)
        results = cur.fetchall()
        response = []
        for result in results:
            response.append(res_to_json(result))
    return flask.jsonify(response)

@app.route("/gtplaces/tags", methods=['GET','POST'])
@login_required
def getTags():
    response = []
    if(request.method=='GET'):
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
    elif(request.method=='POST'):
        bid = request.get_json(force=True)['bid']
        tag = request.get_json(force=True)['tag']
        if(bid=="" or tag==""):
            return flask.jsonify({"error":"Building ID or Tag Name cannot be empty!"}), 400
        query = "insert into tags (b_id,tag_name,gtuser,auth,times_tag,flag_users,times_flagged) values ('"+bid+"','"+tag+"','"+cas.username+"',0,1,'',0) ON DUPLICATE KEY UPDATE times_tag=times_tag+1"
        cur.execute(query)
    return flask.jsonify({"status":"tag inserted"}), 201

@app.route("/gtplaces/tags/<name>", methods=['GET'])
def getByTagName(name):
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
    tag_id = request.get_json(force=True)['tag_id'] # Only flag an existing tag, changing this from the legacy implementation where you could tag by building ID
    if tag_id=="":
        return flask.jsonify({"error":"Tag ID is required"}), 400
    query = "update tags set flag_users = concat(flag_users, '" +cas.username+ ",'), times_flagged=times_flagged+1 where tag_id="+ tag_id
    cur.execute(query)
    return flask.jsonify({"status":"tag flagged"}), 201

app.run(host='0.0.0.0',port=80,debug=True)

