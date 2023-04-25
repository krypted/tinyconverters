import protobuf
import json

def convert_protobuf_to_json(protobuf_message):
  """Converts Protobuf to JSON.

  Args:
    protobuf_message: The Protobuf message to convert.

  Returns:
    The JSON data.
  """

  # Create a JSON object.
  json_data = {}

  # Iterate over the Protobuf message fields.
  for field in protobuf_message.fields:

    # Get the field value.
    value = protobuf_message.get_field(field.name)

    # If the value is a Protobuf message, recursively convert it to JSON.
    if isinstance(value, protobuf.message):
      json_data[field.name] = convert_protobuf_to_json(value)

    # If the value is a string, set the JSON object key to the value.
    elif isinstance(value, str):
      json_data[field.name] = value

    # If the value is an integer, set the JSON object key to the value.
    elif isinstance(value, int):
      json_data[field.name] = value

    # If the value is a float, set the JSON object key to the value.
    elif isinstance(value, float):
      json_data[field.name] = value

    # If the value is a boolean, set the JSON object key to the value.
    elif isinstance(value, bool):
      json_data[field.name] = value

  # Return the JSON data.
  return json_data

"""The Conversion

Passing the prtobuf message to the function.
"""

protobuf_message = protobuf.message()

protobuf_message.set_field("name", "John Doe")
protobuf_message.set_field("age", 30)
protobuf_message.set_field("address", {
  "street": "123 Main Street",
  "city": "Anytown",
  "state": "CA",
  "zip code": 12345
})

json_data = convert_protobuf_to_json(protobuf_message)

print(json_data)

