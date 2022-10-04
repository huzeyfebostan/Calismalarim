"""
Poblem1
Kullanıcıdan alınan boy ve beden kitle indeksini hesaplayan ve şu kurallara göre ekrana şu yazıları yazdırın.
Beden kitle indeksi : Kilo / Boy(m) * Boy(m)
BKİ 18.5'un altındaysa -----> Zayıf
BKİ 18.5 ile 25 arasındaysa -----> Normal
BKİ 25 ile 30 arasındaysa -----> Fazla Kilolu
BKİ 30'un üstündeyse -----> Obez
"""

print("""
****************************
BEDEN KİTLE İNDEKSİ HESAPLAMA PROGRAMI
****************************
""")
"""
kilo = int(input("Kilonuzu Girin:"))
boy = float(input("Boyunuzu Girin:"))

bki = kilo / (boy ** 2)

if (bki<18.5):
    print("Zayıf")
elif (18.5<=bki<25):
    print("Normal")
elif (25<=bki)<30:
    print("Fazla Kilolu")
elif (30<bki):
    print("Obez")
"""

"""
Problem 2
Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.
"""
"""
s1 = int(input("1.Sayıyı Girin:"))
s2 = int(input("2.Sayıyı Girin:"))
s3 = int(input("3.Sayıyı Girin:"))

if (s1 > s2 and s1 > s3):
    print("En büyük sayı {}".format(s1))
elif (s2 > s1 and s2 > s3):
    print("En büyük sayı {}".format(s2))
elif (s3 > s1 and s3 > s2):
    print("En büyük sayı {}".format(s3))
else:
    print("Eşit sayı girme")
"""

"""
Problem 3
Kullanıcının girdiği vize1,vize2 ve final notlarına göre harf notunu hesaplayın:
Vize 1 toplam notun %30'una etki edecek
Vize 2 toplam notun %30'una etki edecek
final toplam notun %40'ına etki edecek
"""

print("""
*************************************
Not Hesaplama Programı
*************************************
""")
"""
v1 = float(input("1.Vize notunu giriniz:"))
v2 = float(input("2.Vize notunu giriniz:"))
f = float(input("Final notunu giriniz:"))

snc = (v1 * 0.3) + (v2 * 0.3) + (f * 0.4)
if (v1 <= 100 and v2 <= 100 and f<=100):
    if (snc >= 90):
        print("AA")
    elif (snc >= 80):
        print("BA")
    elif (snc >= 70):
        print("BB")
    elif (snc >= 60):
        print("CB")
    elif (snc >= 50):
        print("CC")
    elif (snc >= 40):
        print("FF")
else:
    print("0-100 arası not girin")
    
"""
