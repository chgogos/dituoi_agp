package main

import "fmt"

func main() {
	const Pi = 3.14
	fmt.Println(Pi)

	var i1 int8 = 127 // explicit declaration
	// var i1 byte = 127 // το byte είναι alias για το int8
	var i2 int16 = -56
	var i3 int32 = 56
	// var i3 rune = 56 // το rune είναι alias για το int32
	var i4 int64 = 56
	var i5 = 56 // implicit declaration (α' τρόπος)
	i6 := 56 // implicit declaration (β' τρόπος)
	fmt.Println(i1, i2, i3, i4, i5, i6)

	var ui1 uint8 = 127
	var ui2 uint16 = 56
	var ui3 uint32 = 56
	var ui4 uint64 = 56
	fmt.Println(ui1, ui2, ui3, ui4)

	var f1 float32 = 3.14
	var f2 float64 = 3.14
	fmt.Println(f1, f2)

	var s string = "κείμενο στο Ελληνικά"
	fmt.Println(s)

	var b bool = true
	fmt.Println(b)

	var c1 complex64 = 1+2i
	var c2 complex128 = 1+2i
	fmt.Println(c1, c2)
}

