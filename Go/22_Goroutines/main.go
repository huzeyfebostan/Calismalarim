package main

import (
	"fmt"
	"sync"
)

var wg sync.WaitGroup

func main() {
	wg.Add(1)
	go printx()

	wg.Wait()
	printy()

}

func printx() {
	for i := 0; i < 10; i++ {
		fmt.Print("X")
	}
	wg.Done()
}

func printy() {
	for i := 0; i < 10; i++ {
		fmt.Print("Y")
	}
}
