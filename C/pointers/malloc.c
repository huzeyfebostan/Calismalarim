
#include <stdio.h>
#include <stdlib.h>

/*
malloc() fonksiyonunun önüne (int *) yazılmıştır. Bunun nedeni; malloc() fonksiyonun, esnek kullanımı için tipinin void işaretçi
biçiminde yazılmasıdır. Böylece, verdiği bellek alanının başlangıç adresi, her tip işaretçilere atanabilir ve işaretçi aritmetiğinde
yanlışlık olmaz.
p = (int *) malloc(20 * sizeof(int));
biçiminde yazarak, derleyiciye, gelen adresin tamsayı işaretçiye atanacağı ve işaretçi aritmetiğinde dikkatli olması söylenir.
Bu durumda malloc() fonksiyonunun 1000 adresinin gönderdiği varsayılırsa, p + 3 dizinin 4. elemanının adresine, yanı 1006'ya eşittir.
*/

int main()
{
    int *p;
    int i;
    int j;
    int enkucuk;

    p = (int *) malloc(20 * sizeof(int));  // 20 elemanlık yer isteniyor

    for (int i = 0; i < 20; i++)  // rastgele değer atanıyor
    {
        *(p + i) = rand();
        printf("%d.eleman = %d\n",i+1,*(p+i));
    }
    enkucuk = *p;   // ilk eleman en küçük varsayılıyor

    for (int i = 0; i < 20; i++)
        if (*(p + i) < enkucuk) // daha küçüğü var mı
            enkucuk = *(p + i);

    printf("\nEn Küçük elemanı = %d dir\n", enkucuk);
    free(p);    // alınan yer iade ediliyor
}