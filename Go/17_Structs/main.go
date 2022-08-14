/* package main
import "fmt"
func main() {
	var employee struct { // structure
		name      string
		age       int
		isMarried bool
	}
	//fmt.Println(employee)
	//fmt.Printf("%#v\n", employee)
	//fmt.Println(employee.age)
	employee.name = "Ali"
	employee.age = 40
	employee.isMarried = true
	fmt.Printf("%#v\n", employee)
	fmt.Println(employee.name)
	fmt.Println(employee.age)
	fmt.Println(employee.isMarried)
	var employee2 struct { // structure
		name      string
		age       int
		isMarried bool
	}
	employee2.name = "Ela"
	employee2.age = 5
	employee2.isMarried = false
	fmt.Printf("%#v\n", employee2)
	fmt.Println(employee2.name)
	fmt.Println(employee2.age)
	fmt.Println(employee2.isMarried)
} */

/* package main
import "fmt"
type employee struct { // underlying type
	name      string
	age       int
	isMarried bool
}
func main() {
	var e1 employee
	e1.name = "Ali"
	e1.age = 40
	e1.isMarried = true
	var e2 employee
	e2.name = "Ela"
	e2.age = 5
	e2.isMarried = false
	e3 := employee{
		name:      "Deniz",
		age:       3,
		isMarried: false,
	}
	fmt.Printf("%#v\n", e1)
	fmt.Printf("%#v\n", e2)
	fmt.Printf("%#v\n", e3)
} */

/*package main

import "fmt"

type employee struct { // underlying type
	name      string
	age       int
	isMarried bool
	kids      []string
}

func main() {

	e1 := employee{
		name:      "Ali",
		age:       40,
		isMarried: true,
		kids: []string{
			"Ela",
			"Deniz",
		},
	}

	//fmt.Printf("%#v\n", e1)
	fmt.Println(e1)
	fmt.Println(e1.kids)
	fmt.Println(e1.kids[0])

}*/

package main

import "fmt"

type employee struct { // underlying type
	name      string
	age       int
	isMarried bool
}

type manager struct {
	employee
	hasDegree bool
}

// IS A Relation --> Klasik
// HAS A Relation

func main() {

	e1 := employee{
		name:      "Gurcan",
		age:       40,
		isMarried: true,
	}

	fmt.Println(e1)

	/* 	m1 := manager{
		employee: employee{
			name:      "Ayşe",
			age:       28,
			isMarried: false,
		},
		hasDegree: true,
	} */

	m1 := manager{}
	m1.name = "Ayşe"
	m1.age = 28
	m1.isMarried = false
	m1.hasDegree = true

	fmt.Println(m1)

	// Anonim Struct

	theBoss := struct {
		name  string
		money bool
	}{name: "THE BOSS", money: true}

	fmt.Println(theBoss)

}
