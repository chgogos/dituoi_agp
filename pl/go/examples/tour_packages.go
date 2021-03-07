package main

import (
	"fmt"
	"time"
	"math"
	"math/rand"
)

func main() {
	rand.Seed(time.Now().UnixNano())
	fmt.Println("My favorite number is", rand.Intn(10))
	fmt.Println(math.Pi)
}

// My favorite number is 5
// 3.141592653589793