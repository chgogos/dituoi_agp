package main

import (
	"fmt"
	"math"
)

type Vertex struct {
	X, Y float64
}

// η Abs είναι μέθοδος και το receiver όρισμα είναι το v που είναι τύπου Vertex
func (v Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func main() {
	v := Vertex{3, 4}
	fmt.Println(v.Abs())
}
