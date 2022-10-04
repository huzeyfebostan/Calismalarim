""""
1)Kullanıcıdan aldığınız 3 tane  sayıyı çarparak ekrana yazdırın.Ekrana yazdırma işlemini format() metoduyla yapmaya çalışın.
"""
"""
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

print("Sayılar çarpılıyor...")

x1 =a * b * c

print("Birinci Sayı: {}\nİkinci Sayı: {}\nÜçüncü Sayı: {}\nÇarpımları: {}".format(a,b,c,x1))
"""
"""
2)Kullanıcıdan alınan boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.
Beden kitle indeksi:Kilo/(Boy(m)*Boy(m)
"""
"""
boy = float(input("Boy:"))
kilo = int(input("Kilo:"))

print("Değerler alındı hesaplama yapılıyor....")

bki = kilo/(boy*boy)

print ("Girilen bilgiler \nKilo: {}\nBoy: {}\nBeden Kitle İndeksi: {}".format(kilo,boy,bki))
"""

"""
3)Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın be sürücünün toplam ne kadar ödemesi gerektiğini hesaplayın
"""
"""
km = float(input("Araç kilometre'de ne kadar yakıyor:"))
kkm = int(input("Kaç kilometre yol gidildi:"))

snc = km*kkm

print("Araç {} kilometre'de {} tl yakar".format(kkm,snc))
"""

"""
4)Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın
"""
"""
ad = input("Kullanıcının\n Adı:")
soyad = input("Soyadı:")
no = int(input("Telefon Numarası:"))

bilgiler = [ad,soyad,no]

print("Kullanıcının\n Adı:{}\n Soyadı:{}\n Telefon Numarası:{}".format(bilgiler[0],bilgiler[1],bilgiler[2]))
"""

"""
5)Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriye değiştirin
"""
"""
a = int(input("Birinci sayıyı girin:"))
b = int(input("İkinci sayıyı girin:"))

print("Değiştirilmeden önce değerler\n a:{}\n b:{}".format(a,b))

a,b = b,a

print("Değiştirildikten sonra değerler\n a:{}\n b:{}".format(a,b))
"""

"""
6)Kullanıcıdan bir dik üçgenin dik olan iki kenarını (a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.
Hipotenüs formülü:a^2 + b^2 = c^2
"""
"""
a = int(input("Birinci kenar:"))
b = int(input("İkinci kenar:"))

c =(a**2 + b**2) ** 0.5

print("Hipotenüs:{}",c)
"""
