#!/usr/bin/python3
"""

Flask web server creation to handle api petition-requests

"""
from flask import Flask, Blueprint
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def commit_data(error):
        """
        Commit changes in database
        """
        storage.close()

if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000, threaded=True, debug=True)
