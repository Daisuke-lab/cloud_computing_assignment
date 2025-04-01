# Homework 2.2: Managing AWS IAM Roles and Permissions

## Requirements:

* AWS Account

* AWS CLI installed on your computer. Refer the setup guide here `https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html`

 

## Task 1: Create an IAM User

* Create a new IAM user with Access Key. Ensure you save the access key ID and secret access key provided during the creation process.

## Task 2: Create Two IAM Roles

1. Create the first IAM role (S3ReadOnlyAccess):

* Use the AWS Management Console to create a new role.

* Attach the AWS managed policy AmazonS3ReadOnlyAccess to this role.

* Set the trust relationship to allow this role to be assumed by the IAM user created in Task 1, using the following trust policy:

```JavaScript

{

"Version": "2012-10-17",

"Statement": [

{

"Effect": "Allow",

"Principal": {

"AWS": "arn:aws:iam::<Your-Account-ID>:user/<Username>"

},

"Action": "sts:AssumeRole"

}

]

}

```

2. Create the second IAM role (S3FullAccess):

* Use the AWS Management Console to create another new role.

* Create and attach a custom policy that grants full access to a specific S3 bucket (e.g., cloud-computing-assignment-01).

* Configure the trust relationship similar to the first role.

## Task 3: Configure AWS CLI and Test Roles

* Configure the AWS CLI using the access key ID and secret access key of the IAM user you created:

`aws configure`

* Set up profiles in your AWS CLI config file for each role. Add the following entries to `~/.aws/config`, adjusting the role ARN and region as necessary.

```JavaScript

[profile S3ReadOnlyAccess]

role_arn = arn:aws:iam::<Your-Account-ID>:role/S3ReadOnlyAccess

source_profile = default

region = us-east-1

[profile S3FullAccess]

role_arn = arn:aws:iam::<Your-Account-ID>:role/S3FullAccess

source_profile = default

region = us-east-1

```

* Switch to the S3ReadOnlyAccess role and list the contents of the specified S3 bucket:

`aws s3 ls s3://cloud-computing-assignment-01 --profile S3ReadOnlyAccess`

* Test the error "Access Denied":

`aws s3 cp test.txt s3://cloud-computing-assignment-01/test.txt --profile S3ReadOnlyAccess`

* Switch to the S3FullAccess role and try uploading and deleting a file in the S3 bucket:

`echo "Testing full access" > test.txt`

`aws s3 cp test.txt s3://cloud-computing-assignment-01/test.txt --profile S3FullAccess`

`aws s3 rm s3://cloud-computing-assignment-01/test.txt --profile S3FullAccess`

## Submit screenshots demonstrating:

* IAM user and roles configuration pages.

* AWS CLI outputs showing successful execution of the commands in Task 3.