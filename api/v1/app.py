#!/usr/bin/python3
'''Module setting up API'''

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views, states, cities, amenities, users, places, places_reviews
from os import getenv
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins='0.0.0.0')
app.url_map.strict_slashes = False
app.register_blueprint(app_views, url_prefix='/api/v1')

@app.teardown_appcontext
def storage_closer(exceptions):
    ''' closes storage '''
    storage.close()

@app.errorhandler(404)
def page_not_found(e):
        return jsonify({ "error": "Not found" })

if __name__ == "__main__":
    app.run(host=('0.0.0.0'),
            port=(5000))
