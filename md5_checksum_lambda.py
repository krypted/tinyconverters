import json
import hashlib

def calculate_json_checksum(event, context):
    # Retrieve the JSON document from the Lambda event
    json_document = event['body']

    # Load the JSON document
    try:
        data = json.loads(json_document)
    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'body': 'Invalid JSON document'
        }

    # Calculate the MD5 checksum of the JSON document
    checksum = hashlib.md5(json_document.encode()).hexdigest()

    return {
        'statusCode': 200,
        'body': checksum
    }
