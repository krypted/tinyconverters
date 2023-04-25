package main

import (
    "fmt"
    "encoding/hex"
)

func main() {
    // Get the hex string from the user.
    fmt.Print("Enter a hex string: ")
    var hex string
    fmt.Scanln(&hex)

    // Convert the hex string to ASCII.
    ascii, err := hex.DecodeString(hex)
    if err != nil {
        fmt.Println(err)
        return
    }

    // Print the ASCII string.
    fmt.Println("The ASCII representation of", hex, "is", string(ascii))
}

