package main

import (
    "fmt"
    "testing"
    "encoding/hex"
)

func hexToASCII(hex string) (string, error) {
    // Convert the hex string to ASCII.
    ascii, err := hex.DecodeString(hex)
    if err != nil {
        return "", err
    }

    return string(ascii), nil
}

func TestHexToASCII(t *testing.T) {
    // Test cases.
    cases := []struct {
        hex string
        expected string
    }{
        {"48656c6c6f2c20576f726c6421", "Hello, World!"},
        {"74657374206d75737420696e666f", "Testing UnitTests..."},
    }

    // Run the tests.
    for _, tc := range cases {
        actual, err := hexToASCII(tc.hex)
        if err != nil {
            t.Errorf("Error converting hex to ASCII: %v", err)
            continue
        }
        if actual != tc.expected {
            t.Errorf("Expected %s, got %s", tc.expected, actual)
        }
    }
}

func main() {
    // Run the unit tests.
    go test -v
}

