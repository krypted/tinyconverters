# Google Cloud Function To Lint Property Lists

import json
import logging

def lint_property_list(event, context):
    # Get the property list from the event body
    property_list = json.loads(event['body'])

    # Check for errors in the property list
    for key, value in property_list.items():
        if not isinstance(key, str):
            logging.error('Property key must be a string')
            return {'error': 'Property key must be a string'}
        if not isinstance(value, str):
            logging.error('Property value must be a string')
            return {'error': 'Property value must be a string'}

    # The property list is valid, so return success
    return {'success': True}
