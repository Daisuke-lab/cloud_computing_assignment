# Homework 5: Exploring AWS Storage Services

 

## Task 1: Amazon S3 - Setup and Data Management

* Create an Amazon S3 bucket in your AWS account that hosts your static website. Ensure that S3 is public access.

* Create a CloudFront to connect with S3. Ensure that S3 is not public access

## Task 2: Amazon EBS - Volume Creation and Snapshot

* Create an EC2 instance

* Create an EBS volume which is in the same AZ with the above EC2 instance

* Attach the above EBS to the EC2 instance.

* Connect to the EC2 instance and do the following commands:

- List all volumes (list block devices): lsblk

- List all disks (list disk free): df -h

- Format the new volume: sudo mkfs -t xfs /dev/<your-new-ebs>

- Create a mount point: sudo mkdir /mnt/myvolume

- Mount the EBS volume: sudo mount <your-new-ebs> /mnt/myvolume

- Remount automatically after reboot: echo '<your-new-ebs> /mnt/myvolume xfs defaults,nofail 0 2' | sudo tee -a /etc/fstab

## Task 3: Amazon EFS - Setup and Connectivity

* Create another EC2 instance in the same VPC with the previous EC2 instance.

* In the Amazon EFS console create an Amazon EFS file system that is in the same VPC with the above EC2 instances.

* Open inbound traffic on port 2049 (NFS) for Security Group of EFS: Type (NFS), Protocol (TCP), Port: 2049, Source (any IPv4 addresses).

* Connect the EFS to multiple EC2 instances within the same VPC.

- Install amazon-efs-utils: sudo yum install -y amazon-efs-utils

- Create a mount point: sudo mkdir /mnt/efs

- Mount the EFS to the EC2: sudo mount -t efs fs-xxxx /mnt/efs

- Remount automatically when rebooting the EC2 by appending this line to /etc/fstab: fs-xxxx:/ /mnt/efs efs defaults,_netdev 0 0

* Create a new text file in the mounted volume from an instance and check that in another instance

## Submission Requirements:

* Screenshots CloudFront, S3, and Website

* Screenshots EBS and outputs of commands in EC2

* Screenshots EFS and outputs of commands in EC2

## Cleanup

* Terminate all EC2 instances.

* Delete the EBS volume.

* Delete the EFS file system.