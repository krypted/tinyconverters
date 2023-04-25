def binary_to_ascii(binary_text):
  ascii_text = ""
  for i in range(0, len(binary_text), 8):
    ascii_text += chr(int(binary_text[i:i + 8], 2))
  return ascii_text

if __name__ == "__main__":
  binary_text = input("Enter binary text: ")
  ascii_text = binary_to_ascii(binary_text)
  print("The ASCII representation of {} is {}".format(binary_text, 
ascii_text))

