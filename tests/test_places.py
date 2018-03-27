"""
pytest integration tests for places API
"""
from http import HTTPStatus

import pytest

from flask import url_for, json

from places.models import Building, Tag, Category

# Test data imported into db_with_data
building1 = Building(
    address = "1 Example Blvd",
    city = "Atlanta, GA, USA",
    b_id = "1",
    # TODO: 'api_id' is in the DB but missing from JSON- should it be included?
    api_id="building-1",
    image_url = "http://image.example.com/1",
    latitude = -84.3891,
    longitude = 33.7771,
    name = "Test Building 1",
    phone_num = "(555) 111-1111",
    # TODO: The DB data seems to have an unneeded, additional set of outer brackets?  What is this format?
    shape_coordinates = "[[[33.777056, -84.3889078], [33.7773726, -84.3889054], [33.7777347, -84.3888919]9438]]]",
    website_url = "http://web.example.com/1",
    zipcode = "30308",
    tags = [
        Tag(
            tag_id = 1,
            b_id = '1',
            tag_name = 'tag1',
            gtuser = 'burdell',
            auth = 0,
            times_tag = 1,
            times_flagged = 0,
            flag_users = None),
    ],
    categories = [
        Category(b_id='1', cat_name='Housing')
    ]
)
building2 = Building(
    address = "2 Example Blvd",
    city = "Atlanta, GA, USA",
    b_id = "2",
    # TODO: 'api_id' is in the DB but missing from JSON- should it be included?
    api_id="building-2",
    image_url = "http://image.example.com/2",
    latitude = -84.3891,
    longitude = 33.7771,
    name = "Test Building 2",
    phone_num = "(555) 111-1111",
    # TODO: The DB data seems to have an unneeded, additional set of outer brackets?  What is this format?
    shape_coordinates = "[[[33.777056, -84.3889078], [33.7773726, -84.3889054], [33.7777347, -84.3888919]9438]]]",
    website_url = "http://web.example.com/1",
    zipcode = "30308",
)
building3 = Building(
    address = "3 Example Blvd",
    city = "Atlanta, GA, USA",
    b_id = "3",
    api_id="building-3",
    image_url = "http://image.example.com/3",
    latitude = -84.3891,
    longitude = 33.7771,
    name = "Test Building 3",
    phone_num = "(555) 111-1111",
    shape_coordinates = "[[[33.777056, -84.3889078], [33.7773726, -84.3889054], [33.7777347, -84.3888919]9438]]]",
    website_url = "http://web.example.com/3",
    zipcode = "30308",
)

# fixture to load test data into the db
@pytest.fixture(scope='session')
def load_test_db(db):
    db.session.add(building1)
    db.session.add(building2)
    db.session.add(building3)
    db.session.commit()


class TestPlacesApi:

    def test_get_buildings_succeeds(self, db, load_test_db, test_client):
        response = test_client.get('/buildings')

        assert 200 == response.status_code

        assert 'application/json' == response.content_type
        response_body = json.loads(response.get_data(as_text=True))

        # 3 items in test DB returned
        assert isinstance(response_body, list)
        assert 3 == len(response_body)

        # validate fields of first item
        response_item = response_body[0]
        assert 13 == len(response_item)
        assert building1.b_id == response_item['b_id']
        assert building1.name == response_item['name']
        assert building1.address == response_item['address']
        assert building1.city == response_item['address2']
        assert building1.image_url == response_item['image_url']
        assert building1.latitude == response_item['latitude']
        assert building1.longitude == response_item['longitude']
        assert building1.phone_num == response_item['phone_num']
        assert building1.shape_coordinates == response_item['shape_coordinates']
        assert building1.website_url == response_item['website_url']
        assert building1.zipcode == response_item['zipcode']
        assert 1 == len(response_item['tags'])
        assert building1.tags[0].tag_name == response_item['tags'][0]

    def test_get_building_with_valid_id_succeeds(self, db, load_test_db, test_client):
        response = test_client.get('/buildings_id/1')

        assert HTTPStatus.OK == response.status_code

        assert 'application/json' == response.content_type
        response_body = json.loads(response.get_data(as_text=True))
        assert isinstance(response_body, dict)

        # validate fields
        assert 13 == len(response_body)
        assert building1.b_id == response_body['b_id']
        assert building1.name == response_body['name']
        assert building1.address == response_body['address']
        assert building1.city == response_body['address2']
        assert building1.image_url == response_body['image_url']
        assert building1.latitude == response_body['latitude']
        assert building1.longitude == response_body['longitude']
        assert building1.phone_num == response_body['phone_num']
        assert building1.shape_coordinates == response_body['shape_coordinates']
        assert building1.website_url == response_body['website_url']
        assert building1.zipcode == response_body['zipcode']
        assert 1 == len(response_body['tags'])
        assert building1.tags[0].tag_name == response_body['tags'][0]
        assert 1 == len(response_body['categories'])
        assert building1.categories[0].cat_name == response_body['categories'][0]

    def test_get_building_with_unknown_id_returns_404(self, db, load_test_db, test_client):
            response = test_client.get('/buildings_id/BAD_ID')
            assert HTTPStatus.NOT_FOUND == response.status_code