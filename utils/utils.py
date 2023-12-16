import json

DATA_FILE = "data/airbnb.json" 

def get_listings():
    """Read listings data"""
    with open(DATA_FILE) as f:
        data = json.load(f)
    return data

def write_listings(listings):
    """Write listings data""" 
    with open(DATA_FILE, "w") as f:
        json.dump(listings, f)