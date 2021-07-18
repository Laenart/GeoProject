import requests
import json

from app import geo_model


def get_park_by_pois():
    try:
        TOKEN = '5b3ce3597851110001cf6248c7e1c042659a4039bd2ddc4a8e21e3d0'
        BUFFER = 1000
        PARK_CATEGORY_ID = 280
        KRASNODAR_BBOX = [[38.966467, 45.035436],
                          [38.994738, 45.052754]
                          ]

        body = {
            "request": "pois",
            "geometry": {
                "buffer": BUFFER,
                "bbox": KRASNODAR_BBOX
            },
            "filters": {"category_ids": [PARK_CATEGORY_ID]}
        }
        headers = {
            'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
            'Authorization': TOKEN,
            'Content-Type': 'application/json; charset=utf-8'
        }

        call = requests.post('https://api.openrouteservice.org/pois', json=body, headers=headers)
        parks_info = json.loads(call.text)

        parks = []
        for item in parks_info[0]['features']:
            coord = item['geometry']['coordinates']
            distance = item['properties']['distance']
            new_park = geo_model(Latitude=coord[1], Longitude=coord[0],
                                 Distance=distance, TypeId=PARK_CATEGORY_ID)
            parks.append(new_park)
        return parks
    except Exception as err:
        print(err)
