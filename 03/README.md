# Homework 3: Exploring AWS Compute Services

 

## Application Reference: https://github.com/Thao-V/simple-react-node-app

 

## Task 1: Deploy an EC2 Instance

 

* Launch an EC2 instance using the AWS Free Tier.

 

* Choose an Amazon Machine Image (AMI): Amazon Linux and create the instance.

 

* Connect to the above EC2 console, then deploy the above backend application:

 

- Install `git`: sudo yum install git -y

 

- Download `NodeJS`: curl -sL https://rpm.nodesource.com/setup_20.x | sudo bash -

 

- Install `NodeJS`: sudo yum install nodejs -y

 

- Install `PM2`: sudo npm install -g pm2

 

- Clone the application: git clone https://github.com/Thao-V/simple-react-node-app

 

- Change the directory: cd simple-react-node-app/backend

 

- Install Node dependencies: npm i

 

- Run the backend in the background: pm2 start app.js

 

* Open the port 8080:

 

- In the `Security` tab of the above instance, click on `Security Groups`

 

- Edit the inbound rule: Protocol: `Custom TCP`, port: 8080, Source: Allow all IPv4 addresses

 

* Open the browser and type: http://<your-instance-ip>:8080

 

* Take all screenshots for the above steps for submission

 

## Task 2: Set Up an Amazon Lightsail Instance

 

* In the Amazon Lightsail Console, create a lightsail instance

 

* Select a Lightsail Instance with only OS "Amazon Linux"

 

* Select the minimum price and create the instance

 

* Connect to the instance and deploy the application similar to the task 1.

 

* Take all screenshots each above steps for submission

 

## Submit all screenshots.

 

## Cleanup:

 

* Stop and Terminate the above instances