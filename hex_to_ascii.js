function hexToASCII(hex) {
  var ascii = "";
  for (var i = 0; i < hex.length; i += 2) {
    ascii += String.fromCharCode(parseInt(hex.substring(i, i + 2), 16));
  }
  return ascii;
}

// Example
var hex = "48656c6c6f2c20576f726c6421";
var ascii = hexToASCII(hex);
console.log("The ASCII representation of " + hex + " is " + ascii);

