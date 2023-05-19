import json

def count_json_fields(event, context):
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

    # Count the number of fields in the JSON document
    num_fields = len(data.keys())

    return {
        'statusCode': 200,
        'body': str(num_fields)
    }
