package main

import "fmt"

type shape interface {
	area() float64
}

type triangle struct {
	t float64
	a float64
}

type rectangle struct {
	r float64
	e float64
}

type square struct {
	s float64
}

func (t triangle) area() float64 {
	return (t.a * t.t) / 2
}

func (s square) area() float64 {
	return (s.s * s.s)
}

func (r rectangle) area() float64 {
	return (r.r * r.e)
}

func printArea(shapes ...shape) {
	for _, shape := range shapes {
		fmt.Println("Alan : ", shape.area())
	}
}

func main() {
	t := triangle{3, 4}
	s := square{4}
	r := rectangle{4, 5}

	printArea(t, s, r)
}
