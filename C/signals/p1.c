#include <stdio.h>
#include <signal.h>
#include <time.h>
#include <unistd.h>

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
  char kr;
  FILE *fp;
  int pid = getpid();
  printf("%d\n",pid);
  signal(SIGUSR2,sh2);
  signal(SIGUSR1,sh1);
  
  while(1)
  {
    fp = fopen("foo","r");
    if (fp != NULL)
    {
      while (!feof(fp))
      {
        kr = getc(fp);
        putchar(kr);
      }
    }
    fclose(fp);
  }
  
  setbuf(stdout,NULL);
  return 0;
}