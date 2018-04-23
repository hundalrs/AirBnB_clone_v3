#!/usr/bin/python3
'''module that returns JSON status "OK"'''

from flask import jsonify, Blueprint
from models import storage

app_views = Blueprint('app_views', __name__)

@app_views.route('/status')
def status():
    '''returns JSON status'''
    return (jsonify({'status':'OK'}))

@app_views.route('/stats')
def stats():
    ''' return number of objects for each class '''
    return jsonify({
            "amenities": storage.count('Amenity'),
            "cities": storage.count('City'),
            "places": storage.count('Place'),
            "reviews": storage.count('Review'),
            "states": storage.count('State'),
            "users": storage.count('User')
    })
