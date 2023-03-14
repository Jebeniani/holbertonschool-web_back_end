#!/usr/bin/env python3
"""he top 10 of the most present IPs in the collection nginx of the database logs"""
from pymongo import MongoClient

client = MongoClient()
db = client.logs
collection = db.nginx

total_logs = collection.count_documents({})

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = [collection.count_documents(
    {"method": method}) for method in methods]

top_ips = collection.aggregate([
    {"$group": {"_id": "$remote_addr", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}},
    {"$limit": 10}
])

print(f"{total_logs} logs")
print("Methods:")
for method, count in zip(methods, method_counts):
    print(f"\t{method}: {count}")
print("Top 10 IPs:")
for i, ip in enumerate(top_ips, 1):
    print(f"\t{i}. {ip['_id']}: {ip['count']}")
