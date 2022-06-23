#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <signal.h>

//CTRL+C tuşlarına basılana kadar programın çalışmasını sağlar.
void sigint_handler(int sig)
{
    printf("CTRL+C tuşuna basıldı.Yakalanan sinyal: %d\n",sig);
    exit(0);
}

int main () 
{
  signal(SIGINT, sigint_handler);
  
  while(1) 
  {
    printf("1 saniye geçti...\n");
    sleep(1); 
  }
  return(0);
}