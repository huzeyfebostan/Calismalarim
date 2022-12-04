#include <stdio.h>

int collatz(int number)
{
  if (number % 2 == 0)
    number = number / 2;
  else
    number = number * 3 + 1;
    
  return number;
}

int main()
{
  int number = 0;
  
  printf("Bir sayı girin: ");
  scanf("%d",&number);

  while (1)
  {
    number = collatz(number);
    printf("%d\n",number);

    if (number == 1)
      break;
  }
}