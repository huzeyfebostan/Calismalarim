
#include <stdio.h>

/*
Aşağıdaki her iki fonksyon da, kendisine gelen n elemanlı bir tamsayı dizinin elemanlarının toplamını hesaplar ve çağırana gönderir.
İlk fonksiyonda dizinin başlangıç adresi p işaretçisine atanmış ve dizi elemanlarına işaretçiyle erişilmiştir.
İkincisinde döngü için sayaç değişkeni kullanılmayıp, for döngüsü içinde dizinin başlangıç adresi p işaretçisine atanmış ve koşul
kısmında adres karşılaştırılması yapılmıştırç
*/

/* tamsayı dizinin elemanlarının toplamını hesaplar */
int topladizi1(int a[], int n)
{
    int *p;
    int toplam;
    int sayac;

    toplam = 0;
    p = &a[0]; // ilk elemanın adresi p'ye atanıyor
    for (sayac = 0; sayac < n; sayac++)
        toplam += *(p + sayac);
    return (toplam);
}

/* bu da tamsayı dizinin elemanlarını toplar */
int topladizi2(int a[], int n)
{
    int *p;
    int toplam;

    toplam = 0;
    for (p = a; p < &a[n]; ++p)
        toplam += *p;
    return (toplam);
}

int main()
{
    int a[5] = {1,2,3,4,5};
    printf("topladizi1 = %d\n",topladizi1(a,5));
    printf("topladizi2 = %d\n",topladizi2(a,5));
}