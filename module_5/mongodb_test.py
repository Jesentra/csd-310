from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ma9xc.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
print("\n -- Pytech COllection List --")
print(db.list_collection_names())