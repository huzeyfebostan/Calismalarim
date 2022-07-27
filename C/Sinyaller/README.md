#Sinyaller
- Genellikle, sinyalleri üreten olaylar üç ana sınıf altında incelenir: hatalar, dış olaylar, doğrudan yapılan istekler.
- Sinyal isimleri `signal.h` başlık dosyasında tanımlanmıştır.

###Yazılım Hatalarının Sinyalleri
- Aşağıdaki sinyaller, bilgisayarın kendi ya da işletim sistemi tarafından ciddi bir yazılım hatası saptandığında üretilir.  
- `int SIGSEV` bu sinyal, bir yazılımın kendine ayrılan bellek bölgesinin dışında okuma ve yazma denemesi yaptığında ya da salt okunur belleğe yazma denemesinde oluşur.(Aslında bu sinyal sadece sistemin bellek koruma mekanizması tarafından saptanabilen, yazılımın kendi alanının dışında çok uzak bölgelere yazmaya çalıştığı durumlarda ortaya çıkar.)
  * **SIGSEV** sinyalinin alındığı bilinen sorunlar: göstericinini bir boş ya da ilklendirilmemiş göstericiye dönüştürülmesi; bir dizinin sonunu kontrol etmeden dizi üzerinde gösterici aritmetiği ile işlem yapılması.
  * Bir göstericinin bir boş göstericiye dönüşmesi durumunu çeşitli sistemler **SIGSEV** ya da **SIGBUS** sinyali ile belirtir.
- `int SIGBUS` bu sinyal geçersiz duruma gelmiş göstericiler kullanılmaya çalışıldığında ortaya çıkar.
  * **SIGSEV** ile farkı; **SIGSEV** sinyalinin geçerli belleğe geçersiz erişimi belirtmesi, **SIGBUS** sinyalinin ise geçersiz bir adrese erişimi belirtmesidir.
  * Kimi zaman **SIGBUS** sinyali göstericinin hatalı hizalama ile kullanıldığı durumlarda da üretilir.
- `int SIGABRT` bu sinyal yazılımın kendisi tarafından saptanan bir hatayı belirtir ve **abort** çağrısı ile raporlanır.

###Sonlandırma Sinyalleri
- Bu sinyaller bir sürece şu veya bu şekilde sonlandırılacağını söyler.
- `int SIGTERM` yazılımın sonlanmasına sebep olan en temel sinyallerden biridir. **SIGKILL** sinyalinin tersine bu sinyal engellenebilir, işleme sokulabilir ya da yoksayılabilir. **kill** kabuk komutu öntanımlı olarak (seçeneksiz kullanımda) **SIGTERM** sinyali üretir.
- `int SIGINT` sinyali, kullanıcı tarafından INTR karakteri (notmalde **C-c** tuşları) tuşlandığında üretilir.
- `int SIGKILL` sinyali bir uygulamanın anında sonlandırılmasında kullanılır. Bu sinyal engellenemez ve yoksayılamaz.

###Çeşitli Sinyaller
- Bu sinyaller başka başka amaçlar için lullanılır. Onları birşeyler için özellikle kullanmıyorsanız hiçbir etkileri yoktur.
- `int SIGUSR1` ve `int SIGUSR2` sinyalleri istediğiniz herhangi bir amaçla kullanabilmeniz için vardır. Onlar için bir sinyal eylemci yazarsanız, basit süreçler arası iletişim için kullanışlıdır.
- `int SIGWINCH` pencere boyutu değişti. Bu sinyal, bazı sistemlerde (GNU dahil), uçbirim sürücüsünün ektanın satır ve sütun sayılarını tutan kaydı değiştiğinde üretilir.

###Basit Sinyal İşleme
- **signal** işlevi, belirli bir sinyal için bir eylem oluşturmayı sağlayan basit bir arayüzdür
```C
sighandler_t signal (int  sinyalnum, sighandler_t eylem)
```
- **signal** işlevi **sinyalnum** sinyali için eylem olarak **eylem** eylemini oluşturur.
- İlk argüman olan **sinyalnum**, denetlenecek davranışın karşılığı olan sinyaldir ve bir sinyal numarası olarak belirtilmelidir.
- İkinci argüman olan **eylem** ise, **sinyalnum** sinyali için kullanılacak eylemi belirtmek için kullanılır.
- **signal** fonksiyonu için daha ayrıntılı [kaynak](https://www.tutorialspoint.com/c_standard_library/c_function_signal.htm)
- `sighandler_t SIG_ERR`bu makronun değeri, **signal** işlevinin dönen bir hata değeri olarak kullanılır.

###Gelişmiş Sinyal İşleme
- **sigaction** işlevi **signal** işlevi ile aynı temel etkiye sahiptir: bir sinyalin süreç tarafından nasıl işleneceği belirtilir. Farklı olarak, sinyalin üretilmesi ve eylemcinin çağrılması ile ilgili çeşitli denetim seçenekleri belirtilebilir.
```C
int sigaction (int sinyalnum, const struct sigaction *restrict eylem, struct sigaction *restrict eski-eylem)
```
- **eylem** argümanı ile **sinyalnum** sinyali için yeni bir eylem belirtilirken, **eski-eylem** argümanı, bu sembolle ilişkili evvelki eylem hakkında bilgi döndürmek için kullanılır.
- Hem **eylem** hem de **eski-eylem** birer boş gösterici olabilir. **eski-eylem** bir boş gösterici ise, **sinyalnum** sinyali ile ilişkili eylem değişmez:bu, bir sinyalin işlenme şeklini değiştirilmeksizin o sinyalin işlenmesi ile ilgili bilgi edinmenizi mümkün kılar.
- **sigaction** başarılı olduğunda **0** ile aksi taktirde **-1** ile döner.

###signal ve sigaction arasındaki etkileşim
- **signal** ve **sigaction** işlevlerini aynı yazılım içinde kullanmak mümkündür. Ancak tuhav bir yolla bu iki işlev birbirinden etkilenir, bu nedenle bu ikisini aynı yazılım içinde kullanıyorsanız dikkatli olmanız gerekir.
- **sigaction** işlevi **signal** işlevinden daha fazla bilgi içerir.
- Bir eylemi kaydedip daha sonra etkinleştirmek için **signal** işlevini kullanırsanız, tekrar kurulan eylemci **sigaction** tarafından yeniden kurulan eylemci kadar düzgün oluşmayacaktır.
- Sonuç olarak, sorunlardan kaçınmak için, yazılımınızda her yerde **sigaction** kullanmışsanız, bir eylemi kaydetmek ve yeniden oluşturmak için yine **sigaction** işlevini kullanın. Hatta, **sigaction** daha genel olduğundan, bir eylem hangi işlev ile kurulmuş olursa olsun, bir eylemi orjinal haliyle saklamak ve yeniden oluşturmak için daima.

###Başka Bir Sürece Sinyal Gönderme
- **kill** işlevi bir sinyalin başka bir sürece gönderilmesi için kullanılır. ismine rağmen, bir sürecin sonlandırılmasına sebep olmaktan farklı birşeyler yapmak için de kullanılabilir.
```C
int kill (pid_t pid, int sinyalnum)
```
- **kill** işlevi **pid** ile belirtilen süreç ya da süreç grubuna **sinyalnum** sinyalini gönderir, **pid** süreç kümlüğünü doğrulamak için sıfır değerini de kullanabilirsiniz.
- **pid > 0** 
  * Belirteci **pid** olan süreç.
- **pid == 0** 
  * Gönderen ile aynı gruptaki süreçlerin tümü.
- **pid < -1**
  * Belirteci **-pid** olan ssüreç grubu.
- **pid == -1**
  * Eğer süreç ayrıcalıklı ise, sinyal, bazı özel sistem süreçleri dışında kalan tüm süreçlere gönderilir. Aksi taktirde, sinyal, aynı etkin kullanıcı kimlikli tüm süreçlere gönderilir.
- Bir süreç `kill (getpid(), sinyal)`gibi bir çağrı ile kendisine bit sinyal gönderebilir ve sinyal engellenmez, sonrasında **kill** dönmeden önce sürece en az bir sinyal (**sinyalnum** yerine beklemede olan engellenmeyen sinyaller gidebilir) gönderir.
- Sinyal gönderme başarılı olduğunda **kill** 0 ile döner. Aksi taktirde sinyal gönderilmemiş demektir ve **-1** ile döner. Eğer **pid** bir sinyalin birden fazla sürece gönderilmesini belirtiyorsa, en azından bir sürece sinyal gönderilebilmişse **kill** sıfır ile dönecektir. Sinyali alan ve alamayan süreçlerin hangileri olduğunu saptayacak bir yöntem yoktur.

###Sinyal Kümeleri
- Sinyal engelleme işlevlerinin tümü **sinyal kümesi** adı verilen bir veri yapısını kullanırlar. Bu işlem iki kademede yapılır: sinyal kümesi oluşturulur ve bir argüman olarak bir kütüphane işlevine aktarılır.
```C
int sigemptyset (sigset_t *küme)
```
- Bu işlev **küme** sinyal kümesini tanımlı hiçbir sinyali içermediği biçimde ilklendirir. Daima **0** ile döner.
```C
int sigaddset (sigset_t *küme, int sinyalnum)
````
- Bu işlev **sinyalnum** sinyalini **küme** sinyali kümesine ekler. **sigaddset**'ler sadece **küme**'yi değiştirir, sinyal engelleme/engellememe yapmaz. Başarılı olursa **0**, aksi taktirde **-1** ile döner.
