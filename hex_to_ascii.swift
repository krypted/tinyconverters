func hexadecimalToASCII(hexadecimal: String) -> String {
  var ascii = ""
  for char in hexadecimal {
    ascii += String(format: "%c", Int(char, radix: 16)!)
  }
  return ascii
}

let hexadecimal = "48656c6c6f2c20576f726c6421"
let ascii = hexadecimalToASCII(hexadecimal)
print("The ASCII representation of \(hexadecimal) is \(ascii)")

