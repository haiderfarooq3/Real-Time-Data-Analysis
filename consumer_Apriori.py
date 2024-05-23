from kafka import KafkaConsumer
import pandas as pd
from itertools import combinations
from pymongo import MongoClient

mongo_uri = "mongodb://localhost:27017"
client = MongoClient(mongo_uri)

# Select/Create database
db = client['Consumer1']

# Select/Create collection (similar to a table)
collection = db['pairs']

# Function to calculate support for itemsets
def calculate_support(df, itemset):
    if not itemset:
        return 0
    itemset_count = df[list(itemset)].all(axis=1).sum()
    return itemset_count / len(df)

# Generate candidate itemsets of size k
def generate_candidates(L_k_minus_1, k):
    return set([i.union(j) for i in L_k_minus_1 for j in L_k_minus_1 if len(i.union(j)) == k])

# Apriori algorithm function
def apriori(transactions, min_support):
    # Generate frequent 1-itemsets
    L_1 = {frozenset([item]) for item in transactions.columns if calculate_support(transactions, [item]) >= min_support}
    L = [L_1]
    k = 2
    
    while True:
        C_k = generate_candidates(L[k-2], k)
        L_k = set()
        
        for candidate in C_k:
            supp = calculate_support(transactions, candidate)
            if supp >= min_support:
                L_k.add(candidate)
                print(f"Frequent {k}-itemset: {set(candidate)}, Support: {supp:.4f}")
                collection.insert_one({"support": supp})
        if not L_k:
            break
        L.append(L_k)
        k += 1
    
    return L

# Kafka consumer setup
consumer = KafkaConsumer(
    'topic4',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='apriori-group'
)

# Collecting data from Kafka
data = []
for message in consumer:
    transaction = eval(message.value.decode('utf-8'))
    data.append(transaction)
    
    # Assuming transactions are dictionaries with item as key and boolean as value
    df = pd.DataFrame(data)
    
    # Execute Apriori every 100 transactions
    if len(data) % 100 == 0:
        print("Executing Apriori on the latest batch of transactions...")
        frequent_itemsets = apriori(df, min_support=0.01)
        print("Updated frequent itemsets:", frequent_itemsets)
