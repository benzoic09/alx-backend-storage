#!/usr/bin/env python3
""" function that changes all topics of a school
document based on the name:"""


def update_topics(mongo_collection, name, topics):
    """ function that changes all topics of a school
    document based on the name:"""
    name = {"name": name}
    topics = {"$set": {"topics": topics}}

    mongo_collection.update_many(name, topics)
