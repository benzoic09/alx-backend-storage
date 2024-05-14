#!/usr/bin/env python3
"""function that lists all documents in a collection:"""
from pymongo.collection import Collection
from typing import List, Dict


def list_all(mongo_collection):
    """function that lists all documents in a collection:"""
    documents = mongo_collection.find()
    if documents.count() == 0:
        return []
    
    return documents
