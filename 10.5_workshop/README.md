# Workshop 3: Deploy a full-stack app (React-nodejs) by serverless architecture

## Image Uploader

1. Source Code: https://github.com/Thao-V/MIU-Seminar-2025-03-Workshop3

2. Refer the code in `backend` for Lambda function using NodeJS. This function creates an s3 presigned url for uploading, logs information to database, and sends a notification using SNS. Update your existing resources to this function to make it work.

* Database Table: ImageUploads {email: String, url: String, datetime: string}

* Create a s3 bucket for containing images.

3. Front End: Refer the code in `image-uploader`

* This simple ReactJS website that includes an email input, file input, and a button. When users click on the button, it will trigger the communication from this client to the backend.

* Update the API URL for this application.

* Follow the steps from the previous workshop to build and deploy the React website using S3 and CloudFront.

4. Update the Lambda function to validate the file type (PNG).

5. (Optional) Implement a process that automatically generates a thumbnail image for each uploaded image and saves it to the thumbnails directory in the S3 bucket. Update the DynamoDB table with the thumbnail's URL.

## Take screenshots to show the following items

1. Backend: DynamoDB, API Gateway, Lambda function, SNS

2. Frontend: S3 for React, CloudFront, S3 for images

3. Deployed website: Show the live website with working image upload functionality.

## Configure CORS for both S3 and API Gateway to allow requests from the deployed React app's domain.

* CORS for S3: https://docs.aws.amazon.com/AmazonS3/latest/userguide/ManageCorsUsing.html

* CORS for API Gateway: https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-cors.html

## Clean up resources to avoid unexpected charge.