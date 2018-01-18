import pymysql
import json
import os

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='places')
cur = conn.cursor()

with open('places.JSON') as data_file:    
    data = json.load(data_file)
    
for each in data:
##    print(each)
##    print("__________________")   
    id = str(each['id'])
    name = str(each['name'])
    try:
        websiteURL = str(each['websiteURL'])
    except KeyError:
        websiteURL = ""
    try:
        imageURL = str(each['imageURL'])
    except KeyError:
        imageURL = ""
    try:
        phone = str(each['phone'])
    except KeyError:
        phone = ""
    try:
        location_latitude = str(each['location']['latitude'])
    except KeyError:
        location_latitude = ""
    try:
        location_longitude = str(each['location']['longitude'])
    except KeyError:
        location_longitude = ""
    try:
        location_shapeCoordinates = str(each['location']['shapeCoordinates'])
    except KeyError:
        location_shapeCoordinates = ""
    try:
        location_address_postalCode = str(each['location']['address']['postalCode'])
    except KeyError:
        location_address_postalCode = ""
    try:
        location_address_city = str(each['location']['address']['city'])
    except KeyError:
        location_address_city = ""
    try:
        location_address_state = str(each['location']['address']['state'])
    except KeyError:
        location_address_state = ""
    try:
        location_address_street = str(each['location']['address']['street'])
    except KeyError:
        location_address_street = ""
    try:
        category_color = str(each['category']['color'])
    except KeyError:
        category_color = ""
    try:
        category_title = str(each['category']['title'])
    except KeyError:
        category_title = ""
    cur.execute('INSERT INTO gtplaces VALUES ("'+id+'", "'+name+'", "'+imageURL+'", "'+websiteURL+'", "'+phone+'", "'+location_latitude+'", "'+location_longitude+'", "'+location_address_postalCode+'", "'+location_address_city+'", "'+location_address_state+'", "'+location_address_street+'", "'+location_shapeCoordinates+'", "'+category_title+'", "'+category_color+'");')
conn.commit()
conn.close()
