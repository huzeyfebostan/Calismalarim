// 1 -) Underlying Type 'int' olacak şekilde kendi veri tipinizi oluşturunuz
// veri tipi ve değerini '10' yazdırınız.

/*package main

import "fmt"

type deneme int

func main() {
	var x deneme

	x = 10
	fmt.Println(x)

}*/

// 2 -) Başlangıç değeri 10 olan bir X değişkeni oluşturun sonrasında
// bulunduğu adres üzerinden y değişkenini tanımlayıp x değerini 20 yapınız.

/*package main

import "fmt"

func main() {
	x := 10
	y := &x
	fmt.Println(x)
	fmt.Println(y)
	*y = 20
	fmt.Println(x)
	fmt.Println(y)
}*/

// 3 -) Underlying Type struct olan Rectangle type oluşturunuz.
// display, area, circumference metodlarını yazınız.

/*package main

import "fmt"

type rectangle struct {
	a, b int
}

func (r rectangle) display() {
	fmt.Println("Kenarları : ", r.a, "ve", r.b, "olan dikdörtgenin")
}

func (r rectangle) area() int {
	return r.a * r.b
}

func (r rectangle) circumference() int {
	return (r.a + r.b) * 2
}

func main() {
	r1 := rectangle{3, 8}
	r1.display()
	fmt.Println("Alanı: ", r1.area())
	fmt.Println("Çevresi: ", r1.circumference())
}*/

// 4-) family aile bireyleri şeklinde veri tipi oluşturalım, underlying struct. Aile bireylerinin hepsini farklı
// şekilde tanımlayınız. Sonrasında for döngüsünde yazdırınız. field age, name, isMarried field.

package main

import "fmt"

type family struct {
	name      string
	age       int
	isMarried bool
}

func showFamily() []family {
	family1 := family{
		name:      "Ali",
		age:       46,
		isMarried: true,
	}

	family2 := family{
		name:      "Nida",
		age:       42,
		isMarried: true,
	}

	family3 := family{
		name:      "Gizem",
		age:       12,
		isMarried: false,
	}

	var family4 family
	family4.name = "Mert"
	family4.age = 7
	family4.isMarried = false

	return []family{family1, family2, family3, family4}
}

func main() {
	families := showFamily()
	for i := 0; i < len(families); i++ {
		fmt.Println(families[i])
	}
}
