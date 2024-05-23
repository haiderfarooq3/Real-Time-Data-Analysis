#!/bin/bash

# Start Zookeeper in a new tab
gnome-terminal --tab --title="Zookeeper" -- bash -c "bin/zookeeper-server-start.sh config/zookeeper.properties"

# Start Kafka Server in a new tab
gnome-terminal --tab --title="Kafka Server" -- bash -c "bin/kafka-server-start.sh config/server.properties"

# Introduce a delay of 5 seconds (adjust as needed)
sleep 6

# Start Producer in a new tab
gnome-terminal --tab --title="Producer" -- bash -c "python3 producer.py"

# Start Consumer in a new tab
gnome-terminal --tab --title="Consumer" -- bash -c "python3 consumer.py"
