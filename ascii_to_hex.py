def text_to_hex(text):
  hex_digits = []
  for char in text:
    hex_digits.append(format(ord(char), "02x"))
  return "".join(hex_digits)

if __name__ == "__main__":
  text = input("Enter text: ")
  hex_text = text_to_hex(text)
  print("The hexadecimal representation of {} is {}".format(text, 
hex_text))

