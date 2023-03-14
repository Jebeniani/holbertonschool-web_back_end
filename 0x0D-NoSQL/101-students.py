#!/usr/bin/env python3
"""function that returns all students sorted by average score"""


def top_students(mongo_collection):
    """top students are through the next round"""
    pipeline = [
        {"$unwind": "$corrections"},
        {"$group": {
            "_id": "$_id",
            "name": {"$first": "$name"},
            "scores": {"$push": "$corrections.score"}
        }},
        {"$project": {
            "name": 1,
            "averageScore": {"$avg": "$scores"}
        }},
        {"$sort": {"averageScore": -1}}
    ]
    return list(mongo_collection.aggregate(pipeline))
