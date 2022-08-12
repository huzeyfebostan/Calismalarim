package main

import "fmt"

func main() {

	/* 	myArr := [3]int{1, 2, 3}
	   	myArr2 := [...]int{1, 2, 3, 4}
	   	fmt.Println(myArr)
	   	fmt.Println(myArr2)
	   	fmt.Println(len(myArr))
	   	fmt.Println(len(myArr2))
	   	var myArr3 [5]int
	   	fmt.Println(myArr3) */

	/* 	mySlc := []int{1, 2, 3} // LITERAL
	   	fmt.Println(mySlc)
	   	fmt.Println(len(mySlc)) */

	/* 	var myArr [4]int
	   	fmt.Println(myArr)
	   	myArr[0] = 5
	   	fmt.Println(myArr) */

	/* 	var mySlc []int
	   	mySlc = make([]int, 4) // MAKE METHOD
	   	fmt.Println(mySlc)
	   	mySlc[0] = 10
	   	fmt.Println(mySlc) */

	/* 	myArr := [3]int{1, 2, 3}
	   	fmt.Println(myArr)
	   	myArr2 := myArr
	   	fmt.Println(myArr2)
	   	myArr2[0] = 100
	   	fmt.Println(myArr2)
		   fmt.Println(myArr)   Pass By Value    */

	/*mySlc := []int{1, 2, 3}
	fmt.Println(mySlc)
	mySlc2 := mySlc
	fmt.Println(mySlc2)
	mySlc2[0] = 33
	fmt.Println(mySlc2)
	fmt.Println(mySlc)*/ // Pass By Reference

	/*mySlc3 := []string{"denemeler", "üzerine", "bir", "takım"}
	mySlc3 = append(mySlc3, "denemeler")
	fmt.Println(mySlc3)*/

	/* 	underArray := [...]int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	   	fmt.Println(underArray)
	   	mySlc := underArray[2:5]
	   	mySlc2 := underArray[:6]
	   	fmt.Println(mySlc2)
	   	mySlc3 := underArray[3:]
	   	fmt.Println(mySlc3)
	   	mySlc4 := underArray[:]
	   	fmt.Println(mySlc4)
	   	fmt.Println(mySlc)
	   	mySlc[0] = 100
	   	fmt.Println(mySlc)
	   	fmt.Println(mySlc2)
		   fmt.Println(mySlc4) */

	/* 	mySlc := []int{1, 2, 3} // mySliceUnderArray
	   	fmt.Println(mySlc) */

	/* 	mySlc = append(mySlc, 4, 5)
	   	fmt.Println(mySlc) */

	/* 	mySlc2 := append(mySlc, 4, 5) // mySlice2UnderArray
	   	fmt.Println(mySlc2)
	   	mySlc[0] = 100
	   	fmt.Println(mySlc)
	   	fmt.Println(mySlc2) */

	/* 	mySlc := []int{1, 2, 3}
	   	mySlc2 := []int{4, 5}
	   	mySlc = append(mySlc, mySlc2...)
	   	fmt.Println(mySlc) */

	/* 	mySlc := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	   	fmt.Println(mySlc)
	   	// mySlc = mySlc[2:]  ilk n elemanı silmek [n:]
	   	// mySlc = mySlc[:len(mySlc)-3] son n elamanı silmek [:len(mySlc)-n]
	   	mySlc = mySlc[2:]
	   	mySlc = mySlc[:len(mySlc)-3]
	   	fmt.Println(mySlc) */

	/* 	var myArr [4]int
	   	fmt.Println(myArr)
	   	var mySlc []int
	   	mySlc = make([]int, 4) // Zero değerler Slice Elemanlarına
	   	fmt.Println(mySlc)
	   	var mySlc2 []bool
	   	mySlc2 = make([]bool, 2) // Zero değerler Slice Elemanlarına
	   	fmt.Println(mySlc2) */

	var mySlc3 []int
	fmt.Printf("%#v", mySlc3)

	fmt.Println()

	mySlc4 := make([]int, 0)
	fmt.Printf("%#v", mySlc4)

}
