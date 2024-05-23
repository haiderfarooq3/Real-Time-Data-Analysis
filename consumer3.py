from kafka import KafkaConsumer
import pandas as pd
from itertools import combinations
from pymongo import MongoClient
from pyspark.sql import SparkSession
from pyspark.sql import DataFrame

mongo_uri = "mongodb://localhost:27017"
client = MongoClient(mongo_uri)

# Select/Create database
db = client['Consumer3']

# Select/Create collection (similar to a table)
collection = db['id']

# Kafka consumer setup
consumer = KafkaConsumer(
    'topic4',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='group4'
)
u=0
#Assigning id to each attribute in the database
data = []
ids=[]
for message in consumer:
    transaction = eval(message.value.decode('utf-8'))
    data.append(transaction)
    for x in data:
        print("ID:",u,"assigned to respective data")
        ids.append(u)
        u=u+1
        collection.insert_one({"id":u,"data":x})
#Fetching data from Database
fetchdata = collection.find()
rdd = sc.parallelize(fetchdata)
#Applying transformations and actions on data
rdd.take(24)
rdd.max()
rdd.collect()
rdd2 = rdd.flatMap(lambda x: x*4)
print(rdd2.first())
rdd3 = rdd2.map(lambda y: (y,4))
print(rdd3.take(4))
rdd3.persist()
rdd4 = rdd3.reduceByKey(lambda x,y: x*y)
sc.stop()
    
