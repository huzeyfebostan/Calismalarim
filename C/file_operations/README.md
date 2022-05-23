#C'de Dosya İşlemleri

- C programlama dilinde, disk dosyasına erişme (okuma ve yazma için) iki farklı yöntemle yapılır.


- **İlki**, üst düzey G/Ç (high level I/O) ya da tamponlanmış G/Ç (buffered I/O) olarak;
- **ikincisi**, alt düzey G/Ç (low level I/O) ya da UNIX benzei G/Ç (UNIX like I/O) olarak adlandırılır.

- Üst düzey G/Ç yönteminde okuma ve yazma işlemi, temelde, karakter düzeyinde
yapılır ve kullanımı alt düzey G/Ç yöntemine göre daha kolaydır.

- Alt düzey G/Ç yöntemi, gerçekte, ANSI C'de desteklenmiyor (SYS V standardında desteklenmektedir);
---
* #### `fopen(dosyaadı, modu)`
  * Dosya açma fonksiyonu, `fopen()`, kendisini çağırana bir adres gönderir: dosya açılmazsa NULL; açılırsa dosya bilgilerinin saklandığı topluluğun başlangıç adresi.

* ##### `fclose(dosyaadı)`,
* ##### `putc(yazılacak karakteri gösteren değişken, dosya işaretçisi)` ve `fputc(yazılacak karakteri gösteren değişken, dosya işaretçisi)`
kullanılarak aynı anda tek karakter yazılır.
---

* `fopen()` dosya modları; Kİ -> kayıt işaretçisi
  * **"r"** -> Yanlızca okuma için açar. Kİ dosya başına konumlanır.
  * **"w"** -> Yanlızca yazma için açar. Eğer aynı isimli dosya varsa, onun içeriği kaybolur; yoksa onu yeni oluşturur.
Kİ dosya başına konumlanır.
  * **"a"** -> Ekleme yapmak için açar. Kİ dosya sonuna konumlanır, eğer dosya yoksa onu konumlandırır.
  * **"r+"** -> Okuma ve yazma için açar. Kİ dosya başına konumlanır.
  * **"w+"** -> "w" ile aynı, ancak okuma da yapabiir.
  * **"a+"** -> Ekleme için açar. Eğer dosya yoksa oluşturur. OKuma ve yazma yapılabilir.
  * Metin ve ikili tipte dosyayı destekleyen işletim sistemlerinde modların yanına b harfi eklenerek,
dosyanın ikili tiple olacağı  belirtilebilir: **"rb"**, **"a+b"** ...




