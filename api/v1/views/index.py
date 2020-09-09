#!/usr/bin/python3
"""

Flask web server creation to handle api petition-requests

"""
from flask import Response
import json
from api.v1.views import app_views


@app_views.route('/status')
def check_status():
        """
        Commit changes in database
        """
        status_dict = {"status": "OK"}
        return Response(json.dumps(status_dict, indent=4) + "\n",
                        mimetype="application/json")
