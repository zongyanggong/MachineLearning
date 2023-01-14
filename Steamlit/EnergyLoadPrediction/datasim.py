import pandas as pd
import pymongo
import json
import time



# Read data dev
file = "energydata_complete.csv"
df = pd.read_csv(file)
# Lowercase the column names
df.columns = [x.lower() for x in df.columns]
# Set datetime index due to time series analysis
# df = df.set_index('date')
df = df[['date', 'appliances', 'lights', 't1', 'rh_1', 't_out', 'press_mm_hg', 'rh_out', 'windspeed', 'visibility', 'tdewpoint']]
# print(df)

init_record = 10000


url = "mongodb+srv://zongyanggong:gongzy0122@cluster0.auf9spo.mongodb.net/?retryWrites=true&w=majority"
# url ="mongodb+srv://toucanfortune:CEZG3Q2VBtLz@toucanfortune.gzo0glz.mongodb.net/?retryWrites=true&writeConcern=majority"
client = pymongo.MongoClient(url)
db = client.lihua_database
# db = client.get_database("database1")
collection = db.data_simulation
collection.drop()
collection.insert_many(json.loads(df[:init_record].T.to_json()).values())

# print(db.list_collection_names())
#
# for item in db.livedata.find():
#     print(item)
# data = pd.DataFrame(list(collection.find()))
# data = data.drop(['_id'], axis=1)
# data = data.set_index('date')
#
# print(data)
while(True):
    time.sleep(5)
    collection.insert_many(json.loads(df[init_record:init_record+1].T.to_json()).values())
    init_record +=1
    print(init_record)





