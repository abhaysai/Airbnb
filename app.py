# app.py
from flask import Flask, request, abort, jsonify
import json
from utils import data_manager

app = Flask(__name__)

@app.route("/listings", methods=["GET"])
def get_listings():
    """Get all listings"""
    # Implementation
    pass

@app.route("/listings/<int:listing_id>", methods=["GET"]) 
def get_listing(listing_id):
    """Get listing by ID"""
    # Implementation
    pass
    
@app.route("/listings", methods=["POST"])
def create_listing():
    """Create new listing"""
    # Implementation
    pass

@app.route("/listings/<int:listing_id>", methods=["PATCH"])
def update_listing(listing_id):
    """Update existing listing"""
    # Implementation
    pass

@app.route("/listings/<int:listing_id>", methods=["DELETE"])  
def delete_listing(listing_id):
    """Delete existing listing"""
    # Implementation 
    pass

@app.route("/listings/search", methods=["POST"])
def search_listings():
    """Search listings"""
    # Implementation
    pass

# Handle 400 and 500 errors
@app.errorhandler(400)
def bad_request():
    return jsonify({
        "error": 400,
        "message": "Bad request"
    }), 400

@app.errorhandler(500)
def server_error():
    return jsonify({
	    "error": 500,
	    "message": "Internal server error"
    }), 500

if __name__ == "__main__":
    app.run(debug=True)