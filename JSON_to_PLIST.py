import json
import plistlib

def main(event, context):
  # Get the JSON data from the event
  json_data = event['data']

  # Convert the JSON data to a property list
  plist_data = plistlib.dumps(json_data)

  # Return the property list data
  return plist_data

"""Call the function with a POST request to the function's URL. For example:

curl -X POST -H "Content-Type: application/json" -d '{
  "name": "Chuck U Farley",
  "age": 17
}' https://us-central1-my-project.cloudfunctions.net/json-to-property-list

The response to the above would then contain the following property list data:

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
<key>name</key>
<string>Chuck U Farley</string>
<key>age</key>
<integer>17</integer>
</dict>
</plist>
"""
