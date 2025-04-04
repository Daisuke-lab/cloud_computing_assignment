# Homework 4: Implementing and Analyzing AWS Networking

## Task 1: VPC

* Create a VPC (VPC1) as follows:

- Support 512 IP addresses

- Create a public subnet with 16 addresses and a public EC2 in it.

- Create a private subnet with 56 addresses and create a private EC2 in it.

- Ensure to create key to ssh to any instance in all VPCs

- Connect from public EC2 to private EC2 using SSH

## Task 2: VPC Connection

* Create another VPC (VPC2): 1 private subnet, 1 private instance

* Ensure to create key to ssh to any instance in all VPCs

* Establish connection between VPC1 and VPC2 by using either VPC Peering

* Connect from public EC2 of VPC1 to private EC2 of VPC2 using SSH

## Submission the below screenshots:

* VPC1

* VPC2

* VPC Peering

* Route Table of the above VPCs

* Subnets of the above VPCs

* Instances

* Terminal to show the connection between EC2

## Cleanup

* Terminate EC2 instances

* Detach and Delete Internet Gateway

* Delete Transit Gateway Attachments

* Delete Transit Gateway

* Delete subnets

* Delete VPCs