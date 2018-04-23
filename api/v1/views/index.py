#!/usr/bin/python3
'''module that returns JSON status "OK"'''

from flask import jsonify, Blueprint


app_views = Blueprint('app_views', __name__)

@app_views.route('/status')
def status():
    '''returns JSON status'''
    return (jsonify({'status':'OK'}))
