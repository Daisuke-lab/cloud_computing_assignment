import json
import io
from PIL import Image
import boto3

BUCKET_NAME = "cloud-computing-workshop-3-images"

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # TODO implement
    for message in event['Records']:
        print("MESSAGE:", message)
        filename = message['Sns']["Message"]
        response = s3_client.get_object(Bucket=BUCKET_NAME, Key=filename)
        new_file_name = f"thumnail_{filename}"
        # Access the object content
        image_data = response['Body'].read()
        image = Image.open(io.BytesIO(image_data))
        width, height = image.size
        new_image = image.resize((width // 2, height // 2))
        in_mem_file = io.BytesIO()
        new_image.save(in_mem_file, format="PNG")
        in_mem_file.seek(0)
        s3_client.upload_fileobj(
            in_mem_file, # This is what i am trying to upload
            BUCKET_NAME,
            f"thumnails/{new_file_name}"
        )
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
