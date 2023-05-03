# Google Cloud Function To Lint YAML

import yaml
import logging

def lint_yaml(event, context):
    # Get the YAML document from the event body
    yaml_document = event['body']

    # Check for errors in the YAML document
    try:
        yaml.safe_load(yaml_document)
    except yaml.YAMLError as e:
        logging.error(e)
        return {'error': e.message}

    # The YAML document is valid, so return success
    return {'success': True}
