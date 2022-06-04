
# İşaretçiler (Pointers)

- İşaretçi, bellek alanındaki bir gözün adresinin saklandığı değişkendir. İşaretçilere, veriler değil de, o verilerin bellekte saklı olduğu bellek gözlerinin başlangıç adresleri atanır.

- Bir işaretçi değişkenin bellekte e kadar yer işgal ettiği, segmentli adresleme kullanılıyorsa derleyicinin bellek modeline göre, doğrusal adresleme (lineer addressing) kullanılıyorsa doğrudan sistemde kullanılan mikroişlemcinin adres uzunluğuna göre belirlenir.

- Yazım biçimi
 `tip *değişkenadı;`

- İşaretçiye bir değişkenin adresini atamak için `&` operatörü kullanılır. Bu operatör bir değişkenin önüne konulursa, o değişkenin içeriğiyle değil de, adresiyle ilgileniliyor anlamına gelir.

- Bir işaretçi adının önüne `*` operatörü konulursa, o işaretçinin tuttuğu adres ile değil de, işaret ettiği yerdeki veri ile ilgileniliyor anlamına gelir.

### İşaretçi Aritmetiği

- İşaretçiler kullanılırken, bazen işaret ettiği adres taban olarak alınıp, o adresten daha sonraki ve önceki adreslere erişilmek istenir. Bu gibi durumlarda toplama ve çıkarma operatörleri kullanılır.

- İşaretçiye bir eklemek; bellekte, işaret ettiği veriden hemen sonra gelen verinin adresini hesaplar. İşaretçiye `n` sayısını eklemek, bellekte işaret ettiği veriden sonra gelen `n`. elemanın adresini hesaplar.

```
tip *p;         /* işaretçi bildirimi */
.
.
p++;            /* gerçekte yapılan p = p + sizeof(tip) */
.
.
p = p + n;      /* gerçekte yapılan p = p + n * sizeof(tip) */
.
.
```

### İşaretçiler ve Diziler Arasındaki İlişki

- Dizi adı, aslında dizinin ilk elemanının adresini tutan bir işaretçidir. Bir dizinin herhangi bir elemanına işaretçiyle erişilebilir.
```
char tablo[40], *p, *q;

p = &tablo[0];      /* dizinin ilk elemanının adresi p'ye atanıyor */
p = tablo;          /* dizinin başlangıç adresi p'ye atanıyor */
```
İlk iki satırda yapılan atama işlemi aynıdır.
- `*(p+i)` ile `tablo[i]` aynıdır. Çünkü p, dizinin başlangıç adresini tutmaktadır. p işaretçisine i sayısı eklenerek (i + 1). elemanın adresi hesaplanır.

-iki boyutlu bir dizi (matris) için, atamalar aşağıdakiler gibi olabilir:
```
int A[10][20], *p;
p = A;
p = &A[0][0];
```
`A[i][j]` ile `*(p + (i * 20 + j))` aynıdır

### Dinamik Diziler

- Bir dizi programın başında kaç elemanlı olduğu verilerek bildirilirse, derleyici o dizi için gerekli bellek alanını saklı tutar ve o alan başka amaçlar için kullanılamaz.

- Dizilerle dinamik çalışma; programın yürütülmesi sırasında dizi için gerekli bellek alanının işletim sisteminden istenmesi ve işi bittiğinde geri verilmesidir. Bu amaçla standart kütüphanede `calloc()`, `malloc()`, `realloc()` ve `free()` fonksiyonları vardır.

```
tip *isaret;
.
.
isaret = malloc(100);  /* yer isteniyor */
.
.       (kullanılıyor...)
.
free(isaret);          /* geri veriliyor */
.
.
```

### Tipi İşaretçi Olan Fonksiyonlar

- Bir fonksiyon tanımlanırken, formal parametreleri işaretçi olduğu gibi, tipi de işaretçi olabilir. Bu, o fonksiyonun kendisini çağırana bir adres gönderecek anlamına gelir.

- Tipi işaretçi olan fonksiyon ana programda kullanılırken, bu fonksiyondan adres geleceğinden, gelen veri bir işaretçiye atanır ve öyle kullanılır.


