#include <stdlib.h>
#include <stdio.h>
#include <string.h>

//bitwise not
int main()
{
    int x;
    printf("bir tam sayi giriniz: ");
    scanf("%d", &x);

    printf("x = %d\n", x << 4 >> 8);
}