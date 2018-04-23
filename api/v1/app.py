#!/usr/bin/python3
'''Module setting up API'''

from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')

@app.teardown_appcontext
def storage_closer():
    ''' closes storage '''
    storage.close()

if __name__ == "__main__":
    app.run(host=(getenv('HBNB_API_HOST', '0.0.0.0')),
            port=(getenv('HBNB_API_PORT', port=5000)))
