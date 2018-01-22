import json
import pymysql
import flask
from flask import request
from flask_cas import CAS, login_required
import os

app = flask.Flask(__name__)
CAS(app)
app.config['CAS_SERVER'] = 'https://cas-test.gatech.edu/cas'
app.config['CAS_VALIDATE_ROUTE'] = '/serviceValidate'
app.config['SECRET_KEY'] = '6d4e24b1bbaec5f6f7ac35878920b8ebdfdf71bc53521f31bc4ec47885de610d' #set a random key, otherwise the authentication will throw errors
app.config['SESSION_TYPE'] = 'filesystem'
app.config['CAS_AFTER_LOGIN'] ='root' 
conn = pymysql.connect(host='db0.rnoc.gatech.edu', port=3306, user=os.environ['DB_USERNAME'], passwd=os.environ['DB_PASSWORD'], db='CORE_gtplaces')
cur = conn.cursor()

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
def getTags():
    response = []
    if(request.method=='GET'):
        query = "select * from tags"
        cur.execute(query)
        results = cur.fetchall()
        for result in results:
            response.append({
                "tag_id": row[0],
                "b_id": row[1],
                "tag_name": row[2],
                "gtuser": row[3],
                "auth": row[4],
                "times_tag": row[5],
                "flag_users": row[6],
                "times_flagged": row[7]
                })
    elif(request.method=='POST'):
        category = request.get_json()['bid']
        tag = request.get_json()['tag']
##        query = "insert into tags ( where c.cat_name = '"+category+"' and c.b_id = b.b_id"
##        cur.execute(query)
##        results = cur.fetchall()
##        response = []
##        for result in results:
##            response.append(res_to_json(result))
    return flask.jsonify(response)

app.run(host='0.0.0.0', debug=True)    

