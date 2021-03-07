package main

import (
	"fmt"

	"rsc.io/quote"
)

func main() {
	fmt.Println("Hello")

	// χρήση του module quote
	fmt.Println(quote.Go())
	fmt.Println(quote.Glass())
	fmt.Println(quote.Hello())
	fmt.Println(quote.Opt())
}
