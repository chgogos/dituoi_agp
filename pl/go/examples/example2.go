package main

import "fmt"

func main() {
	var v int = 139
	fmt.Printf("%T\n", v)
	fmt.Printf("%v\n", v)
	fmt.Printf("%b\n", v)
	fmt.Printf("%o\n",v)
	fmt.Printf("%x\n",v)
	fmt.Printf("%X\n",v)

	var s string = fmt.Sprintf("%s %v", "test", 123)
	fmt.Println(s)
}


