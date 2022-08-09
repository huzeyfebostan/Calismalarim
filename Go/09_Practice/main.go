// 1-) 1 ile 10 arasındaki sayıları if yapısıyla tek - çift olarak yazdırınız.

/*package main

import "fmt"

func main() {
	for x := 1; x <= 10; x++ {
		if x%2 == 0 {
			fmt.Printf("%d Çift\n", x)
		} else {
			fmt.Printf("%d Tek\n", x)
		}
	}
}*/

//2-) for yapısını kullanarak Go'da olmayan while döngüsüne örnek veriniz.

/*package main

import "fmt"

func main() {
	x := 0

	for x <= 10 {
		fmt.Printf("%d\n", x)
		x++
	}
}*/

//3-) 1 ile 50 arasındaki asal sayıları gösteren bir program yazınız.

package main

import "fmt"

func main() {
	flag := false
	for i := 2; i <= 50; i++ {
		for x := 2; x <= i/2; x++ {
			if i%x == 0 {
				flag = true
				break
			}
		}
		if flag == false {
			fmt.Printf("%d Asal sayıdır\n", i)
		}
		flag = false
	}
}
