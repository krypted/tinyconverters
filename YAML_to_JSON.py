# Basic Google Cloud Function to convert YAML to JSON
import yaml
import json

def main(event, context):
  # Get the YAML data from the event
  yaml_data = event['data']

  # Convert the YAML data to JSON
  json_data = json.dumps(yaml.safe_load(yaml_data))

  # Return the JSON data
  return json_data

"""
Once the function is deployed, call it by sending a POST request to the function's URL with the YAML.

curl -X POST -H "Content-Type: application/yaml" -d '
name: John Doe
age: 30
' https://us-central1-my-project.cloudfunctions.net/yaml-to-json


The response body contains the JSON data as follows:

{
  "name": "John Doe",
  "age": 30
} 
"""
