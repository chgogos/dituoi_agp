package main

import "fmt"

func add(x int, y int) int {
	return x + y
}

func swap(x, y string) (string, string) {
	return y, x
}

func split(sum int) (x, y int) { // named return values
	x = sum * 4 / 9
	y = sum - x
	return  // naked return
}

func main() {
	fmt.Println(add(42, 13))
	a,b :=  swap("hello", "world")
	fmt.Println(a,b)
	fmt.Println(split(17))
}

// 55
// world hello