# BDA_Assignment3_Kafka
Made by:
- Sufyan Nasr i221898
- Haider Farooq i221943
- Muhammad Rayyan Mohsin i222052

# Comprehensive Report: Streaming Data Insights with Frequent Itemset Analysis on Amazon Metadata

## Introduction
This report outlines the methodology, implementation, and outcomes of a project aimed at extracting insights from streaming data using frequent itemset mining techniques on Amazon metadata. The project encompasses various stages including dataset pre-processing, setting up a streaming pipeline, implementing frequent itemset mining algorithms, integrating with a database, and enhancing project execution with a bash script.

## Dataset Description
The Amazon metadata dataset comprises JSON objects with fields such as asin, title, features, description, price, imageURLs, related products, sales rank, brand, categories, and technical details. It provides rich information about Amazon products necessary for analysis and insights generation.

## Pre-Processing
### 1. Loading and Sampling the Dataset
The initial dataset size of 100 GB approximately was sampled to ensure a manageable size for processing, with a minimum sample size of 15 GB maintained to preserve data integrity.

### 2. Data Cleaning and Formatting
The sampled dataset was pre-processed to clean and format the data, making it suitable for analysis. This involved handling missing values, standardizing text formats, and structuring the data for efficient processing.

### 3. Generating Preprocessed Data
A new JSON file containing the preprocessed data was generated, ensuring that it retained all necessary information while being optimized for streaming and analysis.

## Streaming Pipeline Setup
### 1. Producer Application
A producer application was developed to stream preprocessed data in real-time, ensuring a continuous flow of information for analysis.

### 2. Consumer Applications
Three consumer applications were created to subscribe to the producer's data stream, enabling parallel processing and analysis of the streaming data.

## Frequent Itemset Mining
### 1. Apriori Algorithm Implementation
One consumer application implemented the Apriori algorithm, adapting it for the streaming context. Real-time insights and associations were printed to provide immediate feedback on frequent itemsets.

### 2. PCY Algorithm Implementation
Another consumer application implemented the PCY algorithm, leveraging techniques such as sliding window approach and approximation to handle streaming data efficiently. Real-time insights and associations were displayed to facilitate ongoing analysis.

### 3. Innovative Analysis Consumer
The third consumer application was dedicated to innovative and creative analysis. Advanced techniques  In the 3rd consumer, we implemented our own code came up with creative methods and uses for the consumer.

## Database Integration
### Database Selection
A NoSQL database, such as MongoDB, was chosen for its scalability and flexibility, aligning with the requirements of the project.

### Integration with Consumers
Each consumer application was modified to connect to the selected database and store the results, ensuring persistence and accessibility of the generated insights.

## Bonus: Bash Script Enhancement
A bash script was developed to streamline project execution by automating the setup of Kafka components, including Kafka Connect and Zookeeper. This enhancement simplifies the deployment process and improves overall project management.

## Conclusion
The project successfully demonstrated the application of streaming data analysis techniques on Amazon metadata, providing valuable insights into product associations and trends. By leveraging frequent itemset mining algorithms, real-time processing capabilities, database integration, and bash script enhancement, the project achieved its objectives of extracting actionable insights from streaming data in an efficient and scalable manner.

Overall, the project showcases the potential of data mining and streaming analytics in deriving meaningful insights from large-scale datasets, with applications spanning e-commerce, marketing, and consumer behavior analysis.
