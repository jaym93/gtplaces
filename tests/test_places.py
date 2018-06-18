"""
pytest integration tests for places API
"""
from http import HTTPStatus

import pytest
from flask import json

from api.models import Building, Tag, Category

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
        Category(b_id='1', cat_name='Housing'),
        Category(b_id='1', cat_name='Greek')
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
    name = "Another Test Building 3",
    phone_num = "(555) 111-1111",
    shape_coordinates = "[[[33.777056, -84.3889078], [33.7773726, -84.3889054], [33.7777347, -84.3888919]9438]]]",
    website_url = "http://web.example.com/3",
    zipcode = "30308",
)

# in production the WSO2 API Manager will provide a token for endpoints requiring auth
WSO2_AUTH_HEADER = 'X-JWT-Assertion'
WSO2_AUTH_USER_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik51NmZ6bDRiaktOOU85YnBDOTV5VERzSUNoMCJ9.eyJodHRw' \
                       'OlwvXC93c28yLm9yZ1wvY2xhaW1zXC91c2VybmFtZSI6ImpqMTQxIiwiaHR0cDpcL1wvd3NvMi5vcmdcL2NsYWltc1wvc' \
                       'm9sZSI6IkludGVybmFsXC9ldmVyeW9uZSIsImh0dHA6XC9cL3dzbzIub3JnXC9jbGFpbXNcL2FwcGxpY2F0aW9udGllci' \
                       'I6IlVubGltaXRlZCIsImh0dHA6XC9cL3dzbzIub3JnXC9jbGFpbXNcL2tleXR5cGUiOiJQUk9EVUNUSU9OIiwiaHR0cDp' \
                       'cL1wvd3NvMi5vcmdcL2NsYWltc1wvdmVyc2lvbiI6IjEuNSIsImlzcyI6IndzbzIub3JnXC9wcm9kdWN0c1wvYW0iLCJo' \
                       'dHRwOlwvXC93c28yLm9yZ1wvY2xhaW1zXC9hcHBsaWNhdGlvbm5hbWUiOiJEZWZhdWx0QXBwbGljYXRpb24iLCJodHRwO' \
                       'lwvXC93c28yLm9yZ1wvY2xhaW1zXC9lbmR1c2VyIjoiR0FURUNILkVEVVwvamoxNDFAY2FyYm9uLnN1cGVyIiwiaHR0cD' \
                       'pcL1wvd3NvMi5vcmdcL2NsYWltc1wvZW5kdXNlclRlbmFudElkIjoiLTEyMzQiLCJodHRwOlwvXC93c28yLm9yZ1wvY2x' \
                       'haW1zXC9mdWxsbmFtZSI6WyJKb2huc29uIiwiIEplcmVteSBNIl0sImh0dHA6XC9cL3dzbzIub3JnXC9jbGFpbXNcL3N1' \
                       'YnNjcmliZXIiOiJybm9jbGFic3RhZmYiLCJodHRwOlwvXC93c28yLm9yZ1wvY2xhaW1zXC90aWVyIjoiVW5saW1pdGVkI' \
                       'iwiaHR0cDpcL1wvd3NvMi5vcmdcL2NsYWltc1wvZW1haWxhZGRyZXNzIjoiamVyZW15QGltdGMuZ2F0ZWNoLmVkdSIsIm' \
                       'h0dHA6XC9cL3dzbzIub3JnXC9jbGFpbXNcL2FwcGxpY2F0aW9uaWQiOiIxIiwiaHR0cDpcL1wvd3NvMi5vcmdcL2NsYWl' \
                       'tc1wvdXNlcnR5cGUiOiJBUFBMSUNBVElPTl9VU0VSIiwiZXhwIjoxNTI5MzQyNTIzLCJodHRwOlwvXC93c28yLm9yZ1wv' \
                       'Y2xhaW1zXC9hcGljb250ZXh0IjoiXC9ndHBsYWNlc1wvMS41In0=.SHMt/wxqfbnKSMP1XAqX5y3+ZArsaGhvuhC0qRf7' \
                       'E82yZ9g0Yx8p/Yi4wtn30N3YscrbfTTWLtY8LlgjPkn8xnDlcH2sRUFJIrvoZDuPVXoeoOl4OH0lIvF1PZxeXtGJzKd1j' \
                       'vA/C/dNtucSJVPYNhNvMudbtFrPLwXP9Z+Y+kOsEvcSJdrfgNuAUAYcU325k/4MMxQZF48/P555s/EZr02tjBRO/hKmA2' \
                       'IIhZFZr3TzXa9KrLtASAtId6APUoiUQvHibXst7mOjXoCYBswjBDbH0iL0xXY7kWY1gb3PPmy9bav/Nv9rT3i2Wb4sgLp' \
                       'IESsZ2oAv1ltlKGSLgcUFfA=='

# fixture to load test data into the db
@pytest.fixture(scope='session')
def load_test_db(db):
    db.session.add(building1)
    db.session.add(building2)
    db.session.add(building3)
    db.session.commit()


class TestPlacesApi:

    def test_get_buildings_succeeds(self, db, load_test_db, test_client):
        response = test_client.get('/buildings/')

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
        assert 2 == len(response_item['categories'])
        assert building1.categories[0].cat_name == response_item['categories'][0]
        assert building1.categories[1].cat_name == response_item['categories'][1]


    def test_get_buildings_filter_name_succeeds(self, db, load_test_db, test_client):
        response = test_client.get('/buildings/?name=Test%')

        assert 200 == response.status_code

        assert 'application/json' == response.content_type
        response_body = json.loads(response.get_data(as_text=True))
        assert isinstance(response_body, list)

        # returns only buildings from test data that start with "Test"
        assert 2 == len(response_body)
        assert response_body[0]['name'].startswith('Test')
        assert response_body[1]['name'].startswith('Test')

    def test_get_buildings_filter_tag_succeeds(self, db, load_test_db, test_client):
        response = test_client.get('/buildings/?tag=tag1')

        assert 200 == response.status_code

        assert 'application/json' == response.content_type
        response_body = json.loads(response.get_data(as_text=True))
        assert isinstance(response_body, list)

        # returns only 'building1' from test data, tagged with 'tag1'
        assert 1 == len(response_body)
        response_item = response_body[0]
        assert building1.b_id == response_item['b_id']

    def test_get_buildings_filter_category_succeeds(self, db, load_test_db, test_client):
        response = test_client.get('/buildings/?category=Housing')

        assert 200 == response.status_code

        assert 'application/json' == response.content_type
        response_body = json.loads(response.get_data(as_text=True))
        assert isinstance(response_body, list)

        # returns only 'building1' from test data, with category 'Housing'
        assert 1 == len(response_body)
        response_item = response_body[0]
        assert building1.b_id == response_item['b_id']

    def test_get_building_with_valid_id_succeeds(self, db, load_test_db, test_client):
        response = test_client.get('/buildings/1')

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
        assert 2 == len(response_body['categories'])
        assert building1.categories[0].cat_name == response_body['categories'][0]
        assert building1.categories[1].cat_name == response_body['categories'][1]

    def test_get_building_with_unknown_id_returns_404(self, db, load_test_db, test_client):
        response = test_client.get('/buildings_id/BAD_ID')
        assert HTTPStatus.NOT_FOUND == response.status_code

    def test_get_building_tags_succeeds(self, db, load_test_db, test_client):
        response = test_client.get('/buildings/1/tags/')

        assert 200 == response.status_code

        assert 'application/json' == response.content_type
        response_body = json.loads(response.get_data(as_text=True))

        # building 1 has 1 tag
        assert isinstance(response_body, list)
        assert 1 == len(response_body)
        assert 'tag1' == response_body[0]['tag_name']

    def test_get_building_tags_unknown_building_returns_404(self, db, load_test_db, test_client):
        response = test_client.get('/buildings/unknown_building/tags/')

        assert 404 == response.status_code

    def test_get_building_tag_succeeds(self, db, load_test_db, test_client):
        response = test_client.get('/buildings/1/tags/tag1')

        assert 200 == response.status_code

        assert 'application/json' == response.content_type
        response_body = json.loads(response.get_data(as_text=True))

        assert isinstance(response_body, dict)
        assert 'tag1' == response_body['tag_name']

    def test_get_building_tag_unknown_building_returns_404(self, db, load_test_db, test_client):
        response = test_client.get('/buildings/unknown_building/tags/tag1')

        assert 404 == response.status_code

    def test_get_building_tag_unknown_tag_returns_404(self, db, load_test_db, test_client):
        response = test_client.get('/buildings/unknown_building/tags/unknown_tag')

        assert 404 == response.status_code

    def test_get_categories(self, db, load_test_db, test_client):
        response = test_client.get('/categories/')

        assert 200 == response.status_code

        assert 'application/json' == response.content_type
        response_body = json.loads(response.get_data(as_text=True))

        # 2 categories in test data
        assert isinstance(response_body, list)
        assert 2 == len(response_body)
        assert 'Housing' in response_body
        assert 'Greek' in response_body

    def test_get_tags(self, db, load_test_db, test_client):
        response = test_client.get('/tags/')

        assert 200 == response.status_code

        assert 'application/json' == response.content_type
        response_body = json.loads(response.get_data(as_text=True))

        # 1 tag in test data
        assert isinstance(response_body, list)
        assert 1 == len(response_body)
        assert 'tag1' == response_body[0]['tag_name']

    def test_add_new_tag_to_building_succeeds(self, db, load_test_db, test_client):
        response = test_client.post('/buildings/1/tags/', content_type='application/json',
                                    # authenticated endpoint requires token from WSO2 API Manager
                                    headers={WSO2_AUTH_HEADER: WSO2_AUTH_USER_TOKEN},
                                    data=json.dumps({
                                        'tag_name': 'a_new_tag'
                                    }))

        assert 201 == response.status_code

        assert 'application/json' == response.content_type
        response_body = json.loads(response.get_data(as_text=True))

        # new tag object is returned
        assert isinstance(response_body, dict)
        assert 'a_new_tag' == response_body['tag_name']
        assert 'jj141' == response_body['gtuser']

    def test_add_existing_tag_to_building_succeeds(self, db, load_test_db, test_client):
        response = test_client.post('/buildings/1/tags/', content_type='application/json',
                                    # authenticated endpoint requires token from WSO2 API Manager
                                    headers={WSO2_AUTH_HEADER: WSO2_AUTH_USER_TOKEN},
                                    data=json.dumps({
                                        'tag_name': 'tag1'
                                    }))

        assert 201 == response.status_code

        assert 'application/json' == response.content_type
        response_body = json.loads(response.get_data(as_text=True))

        # tag object is returned, tag count incremented
        assert isinstance(response_body, dict)
        assert 'tag1' == response_body['tag_name']
        assert 2 == response_body['times_tag']

    def test_add_new_tag_unknown_building_returns_404(self, db, load_test_db, test_client):
        response = test_client.post('/buildings/some_unknown_building/tags/', content_type='application/json',
                                    # authenticated endpoint requires token from WSO2 API Manager
                                    headers={WSO2_AUTH_HEADER: WSO2_AUTH_USER_TOKEN},
                                    data=json.dumps({
                                        'tag_name': 'a_new_tag'
                                    }))

        assert 404 == response.status_code

    def test_add_tag_without_wso2_auth_fails(self, db, load_test_db, test_client):
        response = test_client.post('/buildings/1/tags/', content_type='application/json',
                                    data=json.dumps({
                                        'tag_name': 'a_new_tag'
                                    }))

        assert 500 == response.status_code

    def test_flag_tag_succeeds(self, db, load_test_db, test_client):
        response = test_client.post('/buildings/1/tags/tag1/flag',
                                    # authenticated endpoint requires token from WSO2 API Manager
                                    headers={WSO2_AUTH_HEADER: WSO2_AUTH_USER_TOKEN})

        assert 201 == response.status_code

        assert 'application/json' == response.content_type
        response_body = json.loads(response.get_data(as_text=True))

        # new tag object is returned
        assert isinstance(response_body, dict)
        assert 'jj141' + ',' == response_body['flag_users']
        assert 1 == response_body['times_flagged']

    def test_flag_tag_unknown_tag_returns_404(self, db, load_test_db, test_client):
        response = test_client.post('/buildings/1/tags/some_unknown_tag/flag',
                                    # authenticated endpoint requires token from WSO2 API Manager
                                    headers={WSO2_AUTH_HEADER: WSO2_AUTH_USER_TOKEN})

        assert 404 == response.status_code

    def test_flag_tag_unknown_building_returns_404(self, db, load_test_db, test_client):
        response = test_client.post('/buildings/some_unknown_building/tags/tag1/flag',
                                    # authenticated endpoint requires token from WSO2 API Manager
                                    headers={WSO2_AUTH_HEADER: WSO2_AUTH_USER_TOKEN})

        assert 404 == response.status_code

    def test_flag_tag_without_wso2_auth_fails(self, db, load_test_db, test_client):
        response = test_client.post('/buildings/1/tags/tag1/flag')

        assert 500 == response.status_code

    def test_internal_flask_error_handling_returns_error_json_and_error_status(self, db, load_test_db, test_client):
        # this tests errors.py error handler registration and correctness of errors.handle_http_error()
        response = test_client.get('/some_url_that_does_not_match_an_api_route')

        assert HTTPStatus.NOT_FOUND == response.status_code
        assert 'application/json' == response.content_type
        response_body = json.loads(response.get_data(as_text=True))
        assert isinstance(response_body, dict)
        assert 2 == len(response_body)
        assert 'message' in response_body
        assert 'status' in response_body

    def test_open_api_documentation_generation_succeeds(self, db, load_test_db, test_client):
        # this tests that Open API specification can at least be extracted by flasgger
        # this can catch some formatting errors
        response = test_client.get('/apispec_1.json')

        assert 200 == response.status_code
        assert 'application/json' == response.content_type