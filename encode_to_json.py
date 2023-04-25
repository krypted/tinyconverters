import json

def decode_json(json_string):
  """Decodes the given JSON string into a Python object.

  Args:
    json_string: The JSON string to decode.

  Returns:
    The Python object.
  """

  # Convert the JSON string to a Python object.
  python_object = json.loads(json_string)

  # Return the Python object.
  return python_object

json_string = """{
  "name": "John Doe",
  "age": 30,
  "address": {
    "street": "123 Main Street",
    "city": "Anytown",
    "state": "CA",
    "zip code": 12345
  }
}"""

python_object = decode_json(json_string)

print(python_object)

