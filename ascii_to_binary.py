def ascii_to_binary(ascii_text):
  binary_text = ""
  for char in ascii_text:
    binary_text += format(ord(char), "08b")
  return binary_text

if __name__ == "__main__":
  ascii_text = input("Enter ASCII text: ")
  binary_text = ascii_to_binary(ascii_text)
  print("The binary representation of {} is {}".format(ascii_text, 
binary_text))
