
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
  int x = 100;
  int sonuc;
  
  printf("%d\n",x);
  sonuc = x << 3;
  printf("%d\n",sonuc);

  return (1);
}