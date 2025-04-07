# Homework 6: Exploring AWS SQL Database Services

## Task 1: Amazon RDS Setup and Basic Operations

* Create an Amazon RDS instance using the MySQL or PostgreSQL engine (depending on the free tier availability).

* Configure the instance to operate within a VPC, ensuring that it is secure and only accessible from your IP address.

* Allow Public Access to test this database.

* Select the smallest DB Instance Size (e.g., db.t3) and then check the monthly cost carefully before clicking on `Create Database`

* Ensure the security group is open for inbound traffic on port 3306 (MySQL).

## Task 2: Connect to the database using EC2

* Create an EC2 in the same VPC with the database

* Install MySql Shell: sudo dnf install -y mariadb105

* Connect to your database using: mysql -h <db-endpoint> -u <user-name> -p

* Create Database: CREATE DATABASE test_db;

* Change to database: use test_db;

* Create a new table:

CREATE TABLE users (

id INT AUTO_INCREMENT PRIMARY KEY,

name VARCHAR(255),

email VARCHAR(255)

);

* Insert data to the above table

INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com'), ('Jane Smith', 'jane@example.com');

* Query data from the table: SELECT * FROM users;

* (Optional) Explore the backup and restore features by creating a manual snapshot and then restoring it to a new instance.

## Task 3: Amazon Aurora Exploration

* Set up an Amazon Aurora cluster using the MySQL-compatible edition.

* Allow Public Access to test this database.

* Select the smallest DB Instance Size (e.g., db.t3) and then check the monthly cost carefully before clicking on `Create Database`.

* Disable `Delete Protection` to cleanup this cluster later.

* Ensure the security group is open for inbound traffic on port 3306 (MySQL).

* (Optional) Test the failover capability by simulating a failover from the Aurora dashboard and observing the downtime.

## Task 4: Do the same as the second task for the Aurora database

 

## Provide a detailed report documenting:

* Screenshot RDS

* Screenshot outputs of all commands in the second task

* Screenshot Aurora

* Screenshot outputs of all commands in the forth task

## Cleanup:

* Delete RDS

* Delete Aurora

* Terminate all EC2