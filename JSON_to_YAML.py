import json
import yaml

def main(event, context):
  # Get the JSON data from the event
  json_data = event['data']

  # Convert the JSON data to YAML
  yaml_data = yaml.safe_dump(json_data, default_flow_style=False)

  # Return the YAML data
  return yaml_data

"""Once deployed, invoke the function with a POST request to the function's URL. To invoke the function:

curl -X POST -H "Content-Type: application/json" -d '{
  "name": "Chuck U Farley",
  "age": 17
}' https://us-central1-my-project.cloudfunctions.net/json-to-yaml


The response would appear as follows:

name: Chuck U Farley
age: 17
"""
