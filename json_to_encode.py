import json

def encode_json(data):
  """Encodes the given data into JSON.

  Args:
    data: The data to encode.

  Returns:
    The JSON string.
  """

  # Convert the data to a JSON object.
  json_object = json.dumps(data)

  # Return the JSON string.
  return json_object

data = {
  "name": "John Doe",
  "age": 30,
  "address": {
    "street": "123 Main Street",
    "city": "Anytown",
    "state": "CA",
    "zip code": 12345
  }
}

json_string = encode_json(data)

print(json_string)

