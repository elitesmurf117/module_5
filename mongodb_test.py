from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.by1b1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";

client = MongoClient (url)

db = client.pytech

print = (db.list_collection_names())

print = ("end of program, press any key to exit..")

