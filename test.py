from dotenv import load_dotenv
import os
import pymongo

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

client = pymongo.MongoClient(MONGO_DB_URL)
db = client["Workshop"]["Network"]
print(list(db.find()))
