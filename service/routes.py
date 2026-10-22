"""Counter routes."""
from flask import jsonify
from service import app

COUNTERS = {}


@app.route("/counters/<name>", methods=["POST"])
def create_counter(name):
    """Create a counter"""
    if name in COUNTERS:
        return jsonify(error=f"Counter {name} already exists"), 409
    COUNTERS[name] = 0
    return jsonify({name: COUNTERS[name]}), 201


@app.route("/counters/<name>", methods=["GET"])
def read_counter(name):
    """Read a counter"""
    if name not in COUNTERS:
        return jsonify(error=f"Counter {name} does not exist"), 404
    return jsonify({name: COUNTERS[name]}), 200


@app.route("/counters/<name>", methods=["PUT"])
def update_counter(name):
    """Increment a counter"""
    if name not in COUNTERS:
        return jsonify(error=f"Counter {name} does not exist"), 404
    COUNTERS[name] += 1
    return jsonify({name: COUNTERS[name]}), 200


@app.route("/counters/<name>", methods=["DELETE"])
def delete_counter(name):
    """Delete a counter"""
    COUNTERS.pop(name, None)
    return "", 204
