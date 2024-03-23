import os
import json
import boto3
import base64
import gzip


def lambda_handler(event, context):
    # Extract email address from environment variables
    sns_topic = os.environ.get('SNS_TOPIC_ARN')

    # Create SNS client
    sns_client = boto3.client('sns')

    log_data = event['awslogs']['data']
    decoded_data = base64.b64decode(log_data)
    decompressed_data = gzip.decompress(decoded_data)
    logs = json.loads(decompressed_data)

    for log in logs['logEvents']:
        log_message = log['message']
        if "error" in log_message.lower():
            # Send email notification
            subject = f"Error Log Notification at {logs['logGroup']}"
            message = f"An error log has been detected:\n\n{log_message}"
            sns_client.publish(
                TopicArn=sns_topic,
                Message=message,
                Subject=subject
            )
