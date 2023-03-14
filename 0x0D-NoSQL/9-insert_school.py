#!/usr/bin/env python3
"""func that inserts a new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """insert with kwargs"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
