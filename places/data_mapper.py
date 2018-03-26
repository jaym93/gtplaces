"""
Maps to/from DB and API JSON representations
"""


def building_db_from_json(building_json):
    db_representation = dict(b_id=building_json.get('b_id'),
                             api_id=building_json.get('api_id'),
                             name=building_json.get('name'),
                             address=building_json.get('address'),
                             city=building_json.get('address2'),
                             zipcode=building_json.get('zipcode'),
                             image_url=building_json.get('image_url'),
                             website_url=building_json.get('website_url'),
                             latitude=building_json.get('latitude'),
                             longitude=building_json.get('longitude'),
                             shape_coordinates=building_json.get('shape_coordinates'),
                             phone_num=building_json.get('phone_num'))
    return db_representation;
