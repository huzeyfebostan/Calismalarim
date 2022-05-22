
#include "stdio.h"
#include "stdlib.h"

/*
Aşağıdaki program, komut satırında girilen dosyanın içindekileri, karakter karakter okur ve ekrana yazar.
Dosyadan okuma yapılacağı için dosya okuma modunda açılmıştır, dosya diskte yoksa NULL adresi gelir.
Bir dosyadan okuma yapılırken dosyanın sonuna gelinip gelinmediği sınanmalıdır. Eğer sınanmadan okuma yapılırsa, o dosyayla 
ilgisi olmayan, diskteki diğer veriler de okunur. Dosya başarılı bir şekilde açıldıktan sonra, bir döngü içinde feof()
fonksiyonu kullanılarak dosya sonu sınanması yapılmıştır. Dosya sonuna gelinmişse, feof() fonksiyonu 0 sayısal değerini 
gönderir. Döngü dosya sonuna gelene kadar tekrarlanır.
*/
//Dosyayı okuma için açma ve içindeki verileri okuma
main(argsay, argdeg)
int argsay;
char *argdeg[];
{
  FILE  *fd;
  char  kr;

  if (argsay < 2)
  {
    printf("Dosya adini girmeyi unuttun !\n");
    exit(0);
  }
  
  if ((fd = fopen(argdeg[1], "r")) == NULL)
  {
    printf("Dosya okuma için açılamadı !\n");
    exit(0);
  }

  /*
  Dosyadan okuma ve ekrana yazma 2 işlemle yapılabilir;
  İlki, feof() kullanarak, okuma yapmadan 
  İkincisi, dosyadan okuma yapıp , onu, dosya sonu karakteriyle karşılaştırarak. EOF 
  */
  
  //feof() dosya sonu sınaması yapar ve dosyanın sonuna gelmişse 0 döndürür
  while (!feof(fd))
  {
    kr = getc(fd);
    putchar(kr);
  }


  //EOF kullanılırsa dikkatli olunmalıdır. Detaylı açıklama için https://www.geeksforgeeks.org/eof-and-feof-in-c/ bak
  // int kr;
  // while ((kr = getc(fd)) != EOF)
  //   putchar(kr);
  
  fclose(fd); 
}