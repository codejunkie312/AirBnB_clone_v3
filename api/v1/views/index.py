#!/usr/bin/python3
"""index view for API"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route("/status", strict_slashes=False)
def status():
    """returns status"""
    return jsonify({"status": "OK"})
