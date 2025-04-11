# Homework 8: Exploring AWS NoSQL Database Services

## Task 1: Amazon DynamoDB - Setup and Data Manipulation

* Create a DynamoDB table named "UserActivity" with a primary key "UserID" (partition key) and "ActivityTime" (sort key).

* Use the AWS Management Console to insert at least 5 items, representing user activities with attributes such as activity type and duration.

* Perform a query to retrieve all activities for a specific user

* Create Lambda function to insert and query data from this table.

## Task 2: Amazon DocumentDB with EC2

* Create an EC2 that allows SSH

* Create a DocumentDB Cluster:

- In the same VPC with the above EC2

- Include the connection to the above EC2

* Connect to the above EC2

- Install Git: sudo yum install git -y

- Install NodeJS: sudo yum install nodejs -y

- Clone the application: git clone https://github.com/Thao-V/aws-basic-apps

- Download the CA for DocumentDB: curl -O https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem

- Copy the above file to the directory `aws-basic-apps/node-docdb`: cp global-bundle.pem aws-basic-apps/node-docdb

- Change the directory to `aws-basic-apps/node-docdb`

- Install dependencies: npm i

- Config .env: URI=<your-connection-string>

- Run the app: node app.js

## Task 3: Amazon ElastiCache - Redis Cache Implementation

1. Set up an ElastiCache Redis cluster in the default VPC

- Select "Design your own cache"

- Select "Cluster Cache"

- Disable "Multi-AZ"

- Choose small "node type" such as "t2.micro"

- Remove "Encryption in Transit"

- Create Cluster

2. Create an EC instance and connect to it:

- Install gcc: sudo yum install gcc

- Download redis-cli: curl -O http://download.redis.io/redis-stable.tar.gz

- Unzip the file: tar xvzf redis-stable.tar.gz

- Change the directory: cd redis-stable

- Install redis-cli: make

- Create redis-cli command: sudo cp src/redis-cli /usr/local/bin/

- Connect to Redis-server: redis-cli -h <cluster-endpoint> -p 6379

- Simple SET command: set <key> <value>

- Simple GET command: get <key>

 

## Submission Requirements:

* Provide detailed documentation of each step taken, including screenshots and descriptions of the setup and queries.

* Submit the scripts or command lines used for creating tables, inserting data, and querying the databases.

 

## Cleanup

* Delete DynamoDB tables

* Delete ElastiCache clusters

* Terminate EC2 instances

* Delete un-used security groups