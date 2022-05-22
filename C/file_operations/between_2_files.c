
#include "stdio.h"
#include "stdlib.h"

/*
Aşağıdaki program, ilk parametrede girilen dosyayı okuyup ikinci parametrede girilen dosyaya yazar eğer öyle bir dosya yoksa 
oluşturup öyle yazar.
*/

main(argsay, argdeg)
int argsay;
char *argdeg[];
{
  FILE  *fd1, *fd2;
  char  kr;

  if (argsay < 3)
  {
    printf("Dosya ad(lar)ını girmeyi unuttun !\n");
    exit(0);
  }
  
  if ((fd1 = fopen(argdeg[1], "r")) == NULL) //Okunmak için ilk dosya açılır
  {
    printf("Dosya okuma için açılamadı !\n");
    exit(0);
  }
  
  if ((fd2 = fopen(argdeg[2], "w")) == NULL) //İlk döngüde açılan dosyanın içindileri yazmak için diğer dosya açılır.
  {
    printf("Dosya yazma için açılamadı !\n");
    exit(0);
  }

  //1.Dosyadan okunur 2.dosyaya yazılır

  while (!feof(fd1))
  {
    kr = getc(fd1);
    putc(kr, fd2);
  }

  fclose(fd1);
  fclose(fd2);

  printf("İşlem tamam\n");
}