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