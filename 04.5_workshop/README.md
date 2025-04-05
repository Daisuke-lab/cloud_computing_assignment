# Workshop 1: AWS VPC & EC2 Hands-on Workshop

## Objective: Design and deploy a secure, two-tier architecture using VPC and EC2, ensuring proper networking and access control.

## Requirements

1. Create a Custom VPC

* Create a new VPC with a CIDR block of 1000 IP addresses starting at 10.10.10.0

* Create two subnets:

- Public subnet (for the web server): 200 Addresses

- Private subnet (for backend services): 500 addresses

2. Deploy a Public EC2 Instance (Web Server)

* Launch an EC2 instance (public instance) in the public subnet and enable Public IP

* Run a default web server with nginx.

- Install nginx: sudo yum install -y nginx

- Run nginx: sudo systemctl start nginx

- Check the status of nginx: sudo systemctl status nginx

* Test your website by this URL: http://<your-instance-ip>

3. Deploy a Private EC2 Instance

* Launch a second EC2 instance (private instance) in the private subnet.

* Launch another server with nginx in this EC2

* Test to ensure that web server is running correctly in this EC2 using the command: curl http://<your-instance-ip>

4. (Optional) Implement the way to connect to web server in the private EC2 from internet.

## Submit

* Screenshot of your VPC (VPC information, Resource Map)

* Screenshot of the Route Table

* Screenshot of subnets.

* Screenshot of your EC2 instances.

* Screenshot of your security group of each instance.

* Screenshot of a successful SSH session from the public instance to the private instance.

* Screenshot of a web page served from the public instance and the private instance.