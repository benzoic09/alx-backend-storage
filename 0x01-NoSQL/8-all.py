#!/usr/bin/env python3
"""function that lists all documents in a collection:"""
"""from pymongo.collection import Collection
from typing import List, Dict """


def list_all(mongo_collection):
    """function that lists all documents in a collection:"""
    return [docs for docs in mongo_collection.find()]
