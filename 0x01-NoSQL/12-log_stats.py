#!/usr/bin/env python3
"""Provides stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def nginx_stats():
    """Provides statistics about the nginx logs."""
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_stats = {method: collection.count_documents(
        {"method": method}) for method in methods}
    status_check = collection.count_documents(
            {"method": "GET", "path": "/status"})

    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_stats[method]}")
    print(f"{status_check} status check")


if __name__ == "__main__":
    nginx_stats()
