#!/usr/bin/python3

"""
Creates the app.
"""

from api.v1.views import app_views
from flask import Flask
from models import storage
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(self):
    """Tears down the storage"""
    storage.close()


if __name__ == "__main__":
    HOST = getenv('HBNB_API_HOST') or '0.0.0.0'
    PORT = getenv('HBNB_API_PORT') or 5000

    app.run(host=HOST, port=PORT, threaded=True)