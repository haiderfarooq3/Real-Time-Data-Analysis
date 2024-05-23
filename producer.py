import json
from kafka import KafkaProducer
from time import sleep

bootstrap_servers = ['localhost:9092']
topic1 = 'topic4'

# Initialize Kafka Producer
producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

# Path to your JSON file
data_path = '/home/sufyan/Documents/Assignment/extracted_data.json'

# Read and send data from JSON file
try:
    with open(data_path, 'r') as file:
        for line in file:
            data = json.loads(line)  # Load each line as a separate JSON object
            producer.send(topic1, value=data)
            print(data)
            sleep(2)  # Delay for 2 seconds

except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")

except KeyboardInterrupt:
    print("Stopping Kafka Producer gracefully")

finally:
    producer.close()  # Ensure the producer is properly closed when the program ends
