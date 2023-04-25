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

    // Convert the ASCII string to binary.
    binary := ""
    for _, char := range ascii {
        binary += strconv.FormatInt(int64(char), 2)
    }

    // Print the binary string.
    fmt.Println("The binary representation of", ascii, "is", binary)
}

