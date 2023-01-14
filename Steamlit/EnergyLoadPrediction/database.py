import os
import pymongo
from dotenv import load_dotenv

load_dotenv(".env")
passwd=os.getenv("passwd")

url =f"mongodb+srv://zongyanggong:{passwd}@cluster0.auf9spo.mongodb.net/?retryWrites=true&w=majority"

# url ="mongodb+srv://toucanfortune:CEZG3Q2VBtLz@toucanfortune.gzo0glz.mongodb.net/?retryWrites=true&writeConcern=majority"
client = pymongo.MongoClient(url)
db = client.lihua_database
# db = client.get_database("database1")
collection = db.test


def insert_period(period,incomes,expenses,comment):
    return collection.insert_one({"key":period, "incomes":incomes, "expenses":expenses,"comment":comment})

def fetch_all_periods():
    return collection.find()

# insert_period("2022_april",1500,600,"some comment")
print(list(fetch_all_periods()))