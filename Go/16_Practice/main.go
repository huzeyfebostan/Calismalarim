// 1 -) 5 string elemandan oluşan array ve 5 int elemandan oluşan slice oluşturup index numaralarıyla göster
/*package main

import "fmt"

func main() {
	strDizi := [5]string{"Huzeyfe", "Yusuf", "Muaz", "Emir", "Ahmet"}

	for index, value := range strDizi {
		fmt.Println(index, value)
	}

	mySlice := []int{1, 3, 5, 6, 8}

	for index, value := range mySlice {
		fmt.Println(index, value)
	}
}*/

//2 -) [0,1,2,3,4,5,6,7,8] slice dan [0,1,2,3], [4,5,6], [6,7,8], [2,3,6,7] slicelarını oluşturunuz.
/*
package main

import "fmt"

func main() {
	firstSlc := []int{0, 1, 2, 3, 4, 5, 6, 7, 8}

	fmt.Println(firstSlc)
	secondSlice := firstSlc[:4]
	fmt.Println(secondSlice)
	thirdSlice := firstSlc[4:]
	thirdSlice = thirdSlice[:len(thirdSlice)-2]
	fmt.Println(thirdSlice)
	fourthSlice := firstSlc[6:]
	fmt.Println(fourthSlice)
	fifthSlice := append(firstSlc[2:4], firstSlc[6:8]...)
	fmt.Println(fifthSlice)
}*/

//4 -) map gösterimi ile takım ve pilotlara ait isimleri for range ile gösterin.

package main

import "fmt"

func main() {
	takimlar := map[string][]string{
		"RedBull":      []string{"Max Verstappen", "Sergio Perez"},
		"Ferrari":      []string{"Charles Leclerc", "Carlos Sainz Jr."},
		"Mercedes":     []string{"Lewis Hamilton", "George Russel"},
		"Alpine":       []string{"Fernando Alonso", "Esteban Ocon"},
		"McLaren":      []string{"Daniel Ricciardo", "Lando Norris"},
		"Alfo Romeo":   []string{"Valtteri Bottas", "Guan Yu Zhou"},
		"Haas":         []string{"Kevin Magnussen", "Mick Schumacher"},
		"AlphaTauri":   []string{"Pierre Gasly", "Yuki Tsunoda"},
		"Aston Martin": []string{"Sebastian Vettel", "Lance Stroll"},
		"Williams":     []string{"Alexander Albon", "Nicholas Latifi"},
	}

	for key, strings := range takimlar {
		fmt.Printf("Takım:%s\n", key)
		fmt.Println("Pilotları:")
		for i, v := range strings {
			fmt.Println("\t", i+1, v)
		}
	}
}
