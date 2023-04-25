function asciiToBinary(ascii) {
  var binary = "";
  for (var i = 0; i < ascii.length; i++) {
    binary += String(ascii.charCodeAt(i)).padStart(8, '0');
  }
  return binary;
}

// Example
var ascii = "Hello, World!";
var binary = asciiToBinary(ascii);
console.log("The binary representation of " + ascii + " is " + binary);

