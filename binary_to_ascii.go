package main

import (
    "fmt"
    "strconv"
)

func main() {
    // Get the binary string from the user.
    fmt.Print("Enter a binary string: ")
    var binary string
    fmt.Scanln(&binary)

    // Convert the binary string to ASCII.
    ascii := ""
    for i := 0; i < len(binary); i += 8 {
        asciiRune, err := strconv.ParseInt(binary[i:i+8], 2, 8)
        if err != nil {
            fmt.Println(err)
            return
        }
        ascii += string(asciiRune)
    }

    // Print the ASCII string.
    fmt.Println("The ASCII representation of", binary, "is", ascii)
}

