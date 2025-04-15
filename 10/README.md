Homework 10: CloudFormation and CodePipeline

## Set Up a CodePipeline

1. Fork the project from: https://github.com/Thao-V/codepipeline-react

2. Create an S3 bucket to contain the build of the above React application as a public web hosting.

3. Set up a new AWS CodePipeline using the AWS Management Console that includes the following configurations:

* Source: Use the above repository as a source.

* Build: Use AWS CodeBuild to build your web application using `buildspec.yml`.

* Deploy: Deploy the application to the above S3 bucket.

4. Ensure the pipeline triggers automatically upon a commit to the source repository.

## Create a CloudFormation Template

1. Create a CloudFormation template in YAML that provisions the following AWS resources:

* An S3 bucket for storing the above project.

* An CloudFront distribution connected to the above S3 bucket

## Submission

* The CloudFormation template

* Screenshots of each pipeline stage configuration.

## Cleanup

* Delete the CodePipeline.

* Delete the CloudFormation Stack.