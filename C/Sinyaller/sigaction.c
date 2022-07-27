#include <signal.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

//sigaction fonksiyonu ile SIGINT sinyali için bir handler fonksiyonu tanımlanır.

void sigint_handler(int sig)
{
  printf("CTRL+C tuşuna basıldı.Yakalanan sinyal: %d\n",sig);
  exit(0);
}

int main()
{
  struct sigaction act;
  act.sa_handler = sigint_handler;
  sigaction(SIGINT, &act, NULL);
  
  while(1)
  {
    printf("1 saniye geçti...\n");
    sleep(1);
  }
  return 0;
}
