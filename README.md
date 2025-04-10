# Homework 7: Advanced AWS Compute Services

## Task 1: Create and Invoke a Simple AWS Lambda Function

* Create a simple AWS Lambda function using the AWS Management Console. The function can be written in Node.js and should perform a basic task (e.g., returning the current date and time) as the below:

```JavaScript

export const handler = async (event) => {

const response = {

statusCode: 200,

body: JSON.stringify({

message: 'Current date and time',

dateTime: new Date().toISOString()

}),

};

return response;

};

```

* Test the function by invoking it manually from the AWS Management Console.

* Set up an API Gateway to trigger the Lambda function via HTTP requests.

## Task 2: Set Up API Gateway

1. Create an API:

* Go to the Amazon API Gateway console.

* Click on “Create API”.

* Select “REST API” and click “Build” under the REST API (not private).

* Choose “New API”, give it a name (e.g., DateTimeAPI), and a description if desired. Then click “Create API”.

2. Create a Resource:

* In the newly created API, under the "Actions" dropdown, select “Create Resource”.

* Enter a resource name and path (e.g., /date-time).

* Click "Create Resource".

3. Create a Method:

* With the new resource selected, under the "Actions" dropdown, select “Create Method”.

* Choose “GET” and click the check mark.

* For the integration type, select “Lambda Function”.

* Check “Use Lambda Proxy integration”.

* Select the region where your Lambda function is located, and type the name of your Lambda function (GetCurrentDateTime).

* Click "Save" and then “OK” to give API Gateway permissions to invoke your Lambda function.

4. Deploy the API:

Under the "Actions" dropdown, select “Deploy API”.

Create a new deployment stage (e.g., prod) and click "Deploy".

5. Test Your API:

* Navigate to the Stages section of your API Gateway, select the stage you deployed to (e.g., prod), and you will see an Invoke URL.

* Access the Invoke URL appended with your resource path (e.g., https://your-api-id.execute-api.region.amazonaws.com/prod/date-time) in a browser or via a tool like Postman to test the API.

## Task 3: Integrate Amazon Cognito with API Gateway

1. Create a Cognito User pool for the app.

* Select "Traditional web application" and name your app "My Web Client"

* Select "email" for sign-in identifiers

* Select "email" for required attributes for sign-up

* Input the return URL: https://localhost:3000

* Create the User Pool

2. Go to details of the created user pool

* Click on Users in User management

* Create a new user with email and password

* Go to App Clients in Applications

* Select the created application

* Go to Login Pages tab

* Edit Manage login pages configuration

* In OAuth 2.0 grant types: replace Authorization code grant by implicit grant. It will ensure that AWS cognito returns the JWT token after logging in.

3. Secure the API using tokens from the Cognito User pool.

* Go to Authorizers in the API Gateway

* Give it a name. Select Cognito as Authorizer type. Select the above user pool. The token source is “Authorization”.

* Go to the resources. Click on the method and click on the “Method request”. Click “Edit” in the Method request settings. In the Authorization select the authorizer. Deploy the API.

4. Test the API

* Go to the above user pool

* Go to App Clients

* Click "View login page"

* After logging in successfully, Iit will redirect you to the callback URL you entered and in the URL you will see `id_token`.

* Copy the ID Token. Provide it in the header as Authorization in Postman when sending a request to the API Gateway.

 

# Submit screenshots demonstrating:

* Lambda function configuration and test results.

* API Gateway configutation and test result.

* Amazon Cognito

* API Gateway configutation and test result after integrating with Amazon Cognito

# Cleanup

* Delete functions from AWS Lambda

* Delete APIs from API Gateway

* Delete Amazon Cognito