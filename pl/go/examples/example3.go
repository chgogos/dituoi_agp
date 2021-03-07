package main

import "fmt"

func main() {
	x := 1
	for x <= 5 {
		fmt.Println(x)
		x++
	}

	for x := 1; x <= 5; x++ {
		fmt.Println(x)
	}

	y := 1
	for {
		fmt.Println(y)
		if y == 5 {
			break
		}
		y++;
	}

}
