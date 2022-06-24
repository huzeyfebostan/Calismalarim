#include <stdio.h>
#include <signal.h>
#include <time.h>

char sym = 'X';
FILE *fp = NULL;

void sh1(int st)
{
  signal(SIGUSR1,sh1);
  fscanf(fp,"%c",&sym);
}

void sh2(int st)
{
  fp = fopen("foo","r");
  setbuf(fp,NULL);
}

int main()
{
  signal(SIGUSR2,sh2);
  signal(SIGUSR1,sh1);
  
  setbuf(stdout,NULL);
  while(1)
    printf("     %c",sym);
  return 0;
}