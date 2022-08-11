// 1 -) Iki rakam arasında toplama, çıkarma ve çarpma
// işleminin yapıldığı bir fonkiyon yazınız.
/*package main

import "fmt"

func main() {
	toplam, fark, carpim := calc(5, 3)
	fmt.Printf("5 + 3 = %d\n5 - 3 = %d\n5 * 3 = %d", toplam, fark, carpim)
}

func calc(num1, num2 int) (int, int, int) {

	toplam := num1 + num2
	fark := num1 - num2
	carpım := num1 * num2

	return toplam, fark, carpım
}*/

// 2 -) Kullanıcı tarafından girilen nota göre geçtiniz
// veya kaldınız geri dönüşünü yazdırınız.
/*
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	fmt.Print("Öğrencinin notunu giriniz: ")
	reader := bufio.NewReader(os.Stdin)
	input, err := reader.ReadString('\n')
	if err != nil {
		fmt.Println(err)
	} else {
		input := strings.TrimSpace(input)
		num, err2 := strconv.Atoi(input)
		if err2 == nil {
			fmt.Println(isPass(num))
		} else {
			fmt.Println(err2)
		}
	}
}

func isPass(value int) string {
	if value >= 0 && value < 20 {
		return "Çok Kötü Not"
	} else if value >= 20 && value < 40 {
		return "Kötü Not"
	} else if value >= 40 && value < 60 {
		return "Orta Not"
	} else if value >= 60 && value < 80 {
		return "İyi Not"
	} else if value >= 80 && value < 100 {
		return "Pekiyi Not"
	} else {
		return "Geçerli Not Giriniz"
	}
}*/

//3 -) 1 ile 100 arasında random gelen sayıyı tahmin etme

package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"strconv"
	"strings"
	"time"
)

func main() {
	randNumber := randNum(1, 100)
	var hak = 10
	for ; hak > 0; hak-- {
		fmt.Println("1 ile 100 arasında bir sayı giriniz ?")
		reader := bufio.NewReader(os.Stdin)
		value, err1 := reader.ReadString('\n')
		if err1 != nil {
			fmt.Println(err1)
		}
		value = strings.TrimSpace(value)
		number, err2 := strconv.Atoi(value)
		if err2 != nil {
			fmt.Println(err2)
		}

		if number < randNumber {
			fmt.Println("Daha büyük bir sayı girin")
		} else if number > randNumber {
			fmt.Println("Daha küçük bir sayı girin")
		} else {
			fmt.Printf("Doğru tahmin\n Sizin tahminininz: %d\n Rastgele üretilen sayı: %d\n", number, randNumber)
			break
		}

		fmt.Printf("Kalan Tahmin Hakkınız: %d\n", hak-1)
	}
	if hak == 0 {
		fmt.Println("Üzgünüz tahmin hakınız bitti")
	}
}

func randNum(min, max int) int {
	rand.Seed(time.Now().Unix())
	return rand.Intn(max-min) + min
}
