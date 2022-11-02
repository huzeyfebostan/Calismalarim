#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>

int main()
{
  int space = 0;
  bool space_flag = false;

  while (1)
  {
    printf("**********");
    delay(100);
    /*space++;
    if (space_flag == false)
    {
      for (int i = space; i >= 0; i--)
      {
        space++; 
        printf(" ");
      }
    }else
    {
      for (int z = 0; z >= space; z++)
      {
        printf(" ");
      }
    }
    if (space == 10)
      space = 0;*/
  }
  
}

void delay(int milliseconds)
{
    long pause;
    clock_t now,then;

    pause = milliseconds*(CLOCKS_PER_SEC/1000);
    now = then = clock();
    while( (now-then) < pause )
        now = clock();
}