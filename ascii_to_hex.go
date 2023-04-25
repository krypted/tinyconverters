package main

import (
    "fmt"
    "strconv"
)

func main() {
    // Get the ASCII string from the user.
    fmt.Print("Enter an ASCII string: ")
    var ascii string
    fmt.Scanln(&ascii)

    // Convert the ASCII string to hex.
    hex := ""
    for _, char := range ascii {
        hex += strconv.FormatInt(int64(char), 16).PadLeft(2, "0")
    }

    // Print the hex string.
    fmt.Println("The hexadecimal representation of", ascii, "is", hex)
}

