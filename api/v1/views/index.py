#!/usr/bin/python3
'''module that returns JSON status "OK"'''

from api.v1.views import app_views
from flask import jsonify


app_views = Blueprint('app_views', __name__)

@app_views.route('/status')
def status():
    '''returns JSON status'''
    return (jsonify({'status':'OK'}))
