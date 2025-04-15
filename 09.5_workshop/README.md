# Workshop 2: Deploy a full-stack app (React-nodejs) with EC2 and auto scaling

## Source code: https://github.com/Thao-V/aws-basic-apps

## Backend

1. The source code for backend in the directory `MIU-Seminar-2025-03-Workshop2/backend`.

2. Use the following script for `User Data` when creating Launch Template. This script will setup and run the backend on port 5005 in EC2.

```

#!/bin/bash

yum install -y git nodejs

npm install -g pm2

cd /home/ec2-user

git clone https://github.com/Thao-V/MIU-Seminar-2025-03-Workshop2

cd MIU-Seminar-2025-03-Workshop2/backend

npm install

sudo -u ec2-user pm2 start index.js --name app

```

3. Important APIs:

* Health check: /health

* Get list of students: /students

* Useful commands to check app running on EC2:

* sudo netstat -tuln | grep :<port>

4. (Optional): Convert the backend to CRUD data from database such as RDS, Aurora or DocumentDB.

5. Infrastructure: ASG -> ALB -> EC2

## Frontend (ReactJS)

* The source code for Frontend in the directory `MIU-Seminar-2025-03-Workshop2/frontend`.

* Follow the file README to run this App locally.

* Build this app by using the command: npm run build

* Copy the content inside the `MIU-Seminar-2025-03-Workshop2/frontend/build` to your S3 bucket

* Infrastructure: CloudFront -> S3

## Take screenshots to show the following items

1. Backend Infrastructure: ASG, ALB, Target Group, Launch Template, EC2

2. Frontend Infrastructure: CloudFront, S3

3. Deployed Website, showing the website running successfully in the browser.

## Cleanup your deployment to avoid any unexpected charge