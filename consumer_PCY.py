import json
from kafka import KafkaConsumer
from collections import defaultdict
import hashlib
from itertools import combinations
from pymongo import MongoClient

mongo_uri = "mongodb://localhost:27017"
client = MongoClient(mongo_uri)

# Select/Create database
db = client['Consumer2']

# Select/Create collection (similar to a table)
collection = db['pairs']

# Define Kafka consumer settings
bootstrap_servers = 'localhost:9092'
topic_name = 'topic4'

# Create a Kafka consumer
consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=bootstrap_servers,
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Helper function to hash itemsets
def hash_itemset(itemset, num_buckets):
    return int(hashlib.sha256(" ".join(sorted(itemset)).encode()).hexdigest(), 16) % num_buckets

# PCY Algorithm implementation
def pcy_algorithm(transactions, support_threshold, num_buckets):
    item_counts = defaultdict(int)
    bucket_counts = defaultdict(int)
    collection.insert_one({"support": support_threshold,"bucketnumber":num_buckets})
    for transaction in transactions:
        # Ensure that transaction is a dictionary
        if isinstance(transaction, dict) and 'items' in transaction:
            items = transaction['items']  # Assuming 'items' contains itemsets
            for item in items:
                item_counts[item] += 1
            for pair in combinations(items, 2):
                bucket_index = hash_itemset(pair, num_buckets)
                bucket_counts[bucket_index] += 1
                print( pair,num_buckets)

    frequent_items = {item for item, count in item_counts.items() if count >= support_threshold}
    frequent_buckets = {bucket for bucket, count in bucket_counts.items() if count >= support_threshold}

    pair_counts = defaultdict(int)
    for transaction in transactions:
        if isinstance(transaction, dict) and 'items' in transaction:
            items = [item for item in transaction['items'] if item in frequent_items]
            for pair in combinations(items, 2):
                if hash_itemset(pair, num_buckets) in frequent_buckets:
                    pair_counts[pair] += 1

    frequent_pairs = {pair for pair, count in pair_counts.items() if count >= support_threshold}
    return frequent_pairs

# Placeholder for storing transactions for batch processing
transaction_buffer = []

# Set parameters for the PCY algorithm
support_threshold = 4
num_buckets = 400

# Process messages from Kafka
for message in consumer:
    transaction_buffer.append(message.value)

    # Perform PCY on the collected transactions periodically
    if len(transaction_buffer) >= 100:
        frequent_itemsets = pcy_algorithm(transaction_buffer, support_threshold, num_buckets)
        print("Frequent itemsets identified:", frequent_itemsets)
        transaction_buffer = []  # Clear buffer after processing
