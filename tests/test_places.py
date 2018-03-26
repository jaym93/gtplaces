import pytest

# Test data imported into db_with_data
from flask import url_for, json

import places
from places import database, routes, data_mapper

building1 = {
    "address": "1 Example Blvd",
    "address2": "Atlanta, GA, USA",
    "b_id": "1",
    "category": [
        "University"
    ],
    "image_url": "http://image.example.com/1",
    "latitude": -84.3891,
    "longitude": 33.7771,
    "name": "Test Building 1",
    "phone_num": "(555) 111-1111",
    # TODO: The DB data seems to have an unneeded, additional set of outer brackets?  What is this format?
    "shape_coordinates": "[[[33.777056, -84.3889078], [33.7773726, -84.3889054], [33.7777347, -84.3888919]9438]]]",
    #"tags": [],
    "website_url": "http://web.example.com/1",
    "zipcode": "30308",
    # TODO: 'api_id' is in the DB but missing from JSON- should it be included?
    "api_id": "building-1"
}

building2 = {
    "address": "2 Example Blvd",
    "address2": "Atlanta, GA, USA",
    "b_id": "21",
    "category": [
        "Housing"
    ],
    "image_url": "http://image.example.com/2",
    "latitude": -84.3891,
    "longitude": 33.7771,
    "name": "Test Building 2",
    "phone_num": "(555) 111-1111",
    "tags": [],
    "website_url": "http://web.example.com/2",
    "zipcode": "30308",
    "api_id": "building-2"
}

building3 = {
    "address": "3 Example Blvd",
    "address2": "Atlanta, GA, USA",
    "b_id": "31",
    "category": [
        "Greek"
    ],
    "image_url": "http://image.example.com/3",
    "latitude": -84.3891,
    "longitude": 33.7771,
    "name": "Test Building 3",
    "phone_num": "(555) 111-1111",
    "tags": [],
    "website_url": "http://web.example.com/3",
    "zipcode": "30308",
    "api_id": "building-3"
}


@pytest.fixture(scope='session')
def loaded_db(db):
    database.create_building(**data_mapper.building_db_from_json(building1));
    database.create_building(**data_mapper.building_db_from_json(building2));
    database.create_building(**data_mapper.building_db_from_json(building3));
    return db


class TestPlacesApi:
    # def test_CheckUser(self):
    #     response = requests.get(config['TEST_Url']+'/checkuser')
    #     self.assertEqual(response.status_code, 200)
    #     response = requests.get(config['TEST_Url']+'/checkuser')  # check for unauthorized here
    #     self.assertEqual(response.status_code, 403)

    def test_get_all_buildings(db, loaded_db, test_client):
        response = test_client.get('/buildings')

        assert response.status_code == 200
        responseJson = response_json(response)

        assert isinstance(responseJson, list)
        assert len(responseJson) == 3

        assert assert_json_equals(responseJson[0], building1)
        assert assert_json_equals(responseJson[1], building2)
        assert assert_json_equals(responseJson[2], building3)

def response_json(response):
    assert response.content_type == 'application/json'
    return json.loads(response.get_data(as_text=True))

def assert_json_equals(json1, json2):
    json1, json2 = json.dumps(json1, sort_keys=True), json.dumps(json2, sort_keys=True)
    assert json1 == json2