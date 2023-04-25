function asciiToHex(ascii) {
  var hex = "";
  for (var i = 0; i < ascii.length; i++) {
    hex += String(ascii.charCodeAt(i)).toString(16).padStart(2, '0');
  }
  return hex;
}

// Example
var ascii = "Hello, World!";
var hex = asciiToHex(ascii);
console.log("The hexadecimal representation of " + ascii + " is " + hex);

