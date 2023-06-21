import json
from pymongo import MongoClient

# MongoDB connection settings
mongo_host = 'localhost'
mongo_port = 27017
mongo_db = 'local'
mongo_collection = 'configurations'

# Path to the JSON file
json_file_path = '/path/to/file.json'

# Connect to MongoDB
client = MongoClient(mongo_host, mongo_port)
db = client[mongo_db]
collection = db[mongo_collection]

# Read JSON file
with open(json_file_path, 'r') as file:
    data = json.load(file)

print(data)

arr = []
arr.append(data)

# Insert documents into MongoDB
collection.insert_many(arr)

# Close MongoDB connection
client.close()

print('JSON data imported successfully.')
