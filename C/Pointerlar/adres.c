
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/*
Aşağıdaki programda, değişkenin adresi ve değeri için aynı değerler iki kez yazılacaktır. İşaretçiye değişkenin adresi atandığı için,
aynı veriyi işaret eder.
*/

int main()
{
    int deg;
    int *isaret;

    deg = 888;
    isaret = &deg;
    printf("Değişkenin adresi = %p\n",isaret);
    printf("Değişkenin değeri = %d\n",*isaret);
    printf("-----------------------\n");
    printf("Değişkenin adresi = %p\n",&deg);
    printf("Değişkenin değeri = %d\n",deg);
}