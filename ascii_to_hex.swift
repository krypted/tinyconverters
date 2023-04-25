func asciiToHexadecimal(ascii: String) -> String {
  var hexadecimal = ""
  for char in ascii {
    hexadecimal += String(format: "%02x", char)
  }
  return hexadecimal
}

let ascii = "Hello, World!"
let hexadecimal = asciiToHexadecimal(ascii)
print("The hexadecimal representation of \(ascii) is \(hexadecimal)")

