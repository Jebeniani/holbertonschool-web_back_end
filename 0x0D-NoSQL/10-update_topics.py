#!/usr/bin/env python3
"""func that changes all topics of a school doc based in the name"""


def update_topics(mongo_collection, name, topics):
    """changes all topics"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
