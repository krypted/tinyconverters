func asciiToBinary(ascii: String) -> String {
  var binary = ""
  for char in ascii {
    binary += String(format: "%08b", char)
  }
  return binary
}

let ascii = "Hello, World!"
let binary = asciiToBinary(ascii)
print("The binary representation of \(ascii) is \(binary)")

