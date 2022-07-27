
#include "stdio.h"
#include "stdlib.h"

//Dosya oluşturma ve döngü içinde, içine veri yazma
/*Aşağıdaki program, adı komut satırında girilen dosyayı yazma modunda açmaya çalışır. Karşılaştırma deyimi içinde fopen() 
fonksiyonunun gönderdiği adres önce fd değişkeninin içine atınır, ardından NULL ile karşılaştırılır. Dosya açılamayacağı
zaman NULL geleceği için ekrana uygun mesaj yazılır ve program sonlanır. Başarılı olarak açılırsa NULL dışında bir değer 
geleceği için, if deyimindeki küme atlanır. Daha sonra bir döngü deyimi içinde, dosyaya yazılacaklar karakter karakter okunur 
ve dosyaya yazılır. Klavyeden 'q' karakteri girilirse, dosyaya yazılmadan, döngü sonlanır. Son olarak da dosya, fclose()
fonksiyonu kullanılarak kapatılır.
*/
//Dosya oluşturma ve döngü içinde, içine veri yazma
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
  
  if ((fd = fopen(argdeg[1], "w")) == NULL)
  {
    printf("Dosya yazma için açılamadı !\n");
    exit(0);
  }
  
  while ((kr = getchar()) != 'q')
    putc(kr, fd);

  fclose(fd); 
}