#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
  pid_t pid = atoi(argv[1]);

  FILE *fp = fopen("foo","w");
  setbuf(fp,NULL);

  kill(pid,SIGUSR2);

  char c;
  while(scanf("%c",&c) == 1)
  {
    if (c == '\n') continue;
    fprintf(fp,"%c",c);
    kill(pid,SIGUSR1);
  }

  unlink("foo");
  kill(pid,SIGTERM);

  return 0;
}