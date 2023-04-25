def hex_to_ascii(hex_text):
  ascii_text = ""
  for char in hex_text:
    ascii_text += chr(int(char, 16))
  return ascii_text

if __name__ == "__main__":
  hex_text = input("Enter hexadecimal text: ")
  ascii_text = hex_to_ascii(hex_text)
  print("The ASCII representation of {} is {}".format(hex_text, 
ascii_text))

