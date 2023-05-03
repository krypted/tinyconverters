# Google Cloud Function To Lint JSON Documents

import json
import logging

def lint_json(event, context):
    # Get the JSON document from the event body
    json_document = json.loads(event['body'])

    # Check for errors in the JSON document
    try:
        json.dumps(json_document, indent=2)
    except json.JSONDecodeError as e:
        logging.error(e)
        return {'error': e.message}

    # The JSON document is valid, so return success
    return {'success': True}
