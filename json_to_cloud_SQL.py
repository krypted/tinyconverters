"""
Puts JSON into a Cloud SQL database.
  Args:
    event: The event object.
    context: The context object.

  Returns:
    A response object.

  To use it, pass the information :
  
curl -X POST \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "json_data": {
      "name": "Charles",
      "email": "charles@chuckufarley.com"
    }
  }' \
  https://us-central1-PROJECT_ID.cloudfunctions.net/put_json_into_database
"""

import os
import json

from google.cloud import sql


def put_json_into_database(event, context):

  # Get the JSON data from the event.
  json_data = json.loads(event['body'])

  # Get the database client.
  db = sql.Client()

  # Get the instance name.
  instance_name = os.environ['INSTANCE_NAME']

  # Get the database name.
  database_name = os.environ['DATABASE_NAME']

  # Get the table name.
  table_name = os.environ['TABLE_NAME']

  # Connect to the database.
  with db.connect(instance_name, database_name) as connection:

    # Insert the JSON data into the table.
    connection.execute(
        'INSERT INTO `{}` ({}) VALUES ({})'.format(
            table_name,
            ', '.join(json_data.keys()),
            ', '.join('?' * len(json_data.keys()))
        ),
        json_data.values()
    )

  # Return the response object.
  return {
    'message': 'The JSON data was successfully put into the database.'
  }
