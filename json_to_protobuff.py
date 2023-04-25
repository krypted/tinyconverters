import json
import protobuf

def convert_json_to_protobuf(json_data):
  """Converts JSON data to Protobuf.

  Args:
    json_data: The JSON data to convert.

  Returns:
    The Protobuf message.
  """

  # Create a Protobuf message.
  message = protobuf.message()

  # Iterate over the JSON data.
  for key, value in json_data.items():

    # If the value is a string, set the Protobuf message field to 
the value.
    if isinstance(value, str):
      message.set_field(key, value)

    # If the value is an object, recursively convert it to a 
Protobuf message.
    elif isinstance(value, dict):
      message.set_field(key, convert_json_to_protobuf(value))

    # If the value is an array, recursively convert each element 
to a Protobuf message.
    elif isinstance(value, list):
      for element in value:
        message.add_element(key, 
convert_json_to_protobuf(element))

  # Return the Protobuf message.
  return message

json_data = {
  "name": "John Doe",
  "age": 30,
  "address": {
    "street": "123 Main Street",
    "city": "Anytown",
    "state": "CA",
    "zip code": 12345
  }
}

protobuf_message = convert_json_to_protobuf(json_data)

print(protobuf_message)

