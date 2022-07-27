#include <stdio.h>

int main()
{
    int x, y;
    printf("iki tamsayi giriniz: ");
    scanf("%d%d", &x, &y);
    printf("ilk sayı: %d\t ikinci sayı: %d\n",x,y);
    x ^= y, y ^= x, x ^= y;
    printf("değişim sonrası ilk sayı = %d\t ikinci sayı: %d \n", x, y);
}