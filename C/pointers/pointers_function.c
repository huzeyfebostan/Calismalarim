
#include <stdio.h>

int *gonder_enkucugun_adresini(int A[], int n)
{
    int enkucuk;
    int *p;
    int i;

    enkucuk = A[0];
    p = &A[0];
    for (i = 1; i < n; i++)
        if (A[i] < enkucuk)
        {
            enkucuk = A[i];
            p = &A[i];
        }
    return (p);
}

int main()
{
    int dizi[] = { 30, 22, 23, 20, 34, 38, 11};
    int *q;

    q = gonder_enkucugun_adresini(dizi, 7);
    printf("En küçük eleman = %d\n", *q);
}