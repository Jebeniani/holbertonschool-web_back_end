#!/usr/bin/env python3
"""function that lists all documents in a collection"""
import pymongo


def list_all(mongo_collection):
    """find all documents in the collection"""
    result = []
    for document in mongo_collection.find():
        result.append(document)
    return result
