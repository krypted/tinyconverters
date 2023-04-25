function binaryToASCII(binary) {
  var ascii = "";
  for (var i = 0; i < binary.length; i += 8) {
    ascii += String.fromCharCode(parseInt(binary.substring(i, i + 8), 2));
  }
  return ascii;
}

// Example
var binary = "10001000 10100100 10110011 10110000 10110001 10101110 
10110100 10111001 10100000 10111000 10110011";
var ascii = binaryToASCII(binary);
console.log("The ASCII representation of " + binary + " is " + ascii);

