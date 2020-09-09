#!/usr/bin/python3
"""

Flask web server creation to handle api petition-requests

"""
from flask import Flask, Blueprint, jsonify
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def commit_data(error):
        """
        Commit changes in database
        """
        storage.close()


@app.errorhandler(404)
def not_found(error):
    """

    Args:
        error: error received

    Returns: Json with data

    """
    my_error_dict = {"error": "Not found"}
    return jsonify(my_error_dict), 404


if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000, threaded=True)
