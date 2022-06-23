"""
1.ALIŞTIRMA
1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.

Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).
"""
"""
def mukemmel(sayi):

    toplam = 0

    for i in range(1,sayi):
        if(sayi % i == 0):
            toplam += i

    return toplam == sayi

for i in range(1,1001):
    if (mukemmel(i)):
        print("Mükemmel Sayılar:",i)
"""

"""
2.ALIŞTIRMA
Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.
"""
"""
def ebob_bulma(sayi1,sayi2):
    
    i = 1
    ebob = 1
    
    while (i<=sayi1 and i<=sayi2):
        
        if (not (sayi1 % i) and not (sayi2 % i)):
            ebob = i
        i += 1
    return ebob

sayi1 = int(input("1.Sayıyı Girin:"))
sayi2 = int(input("2.Sayıyı Girin:"))

print("EBOB:",ebob_bulma(sayi1,sayi2))
"""

"""
3.ALIŞTIRMA
Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.
"""
"""
def ekok_bulma(sayi1,sayi2):

    i = 2
    ekok = 1

    while True:

        if (sayi1 % i == 0 and sayi2 % i == 0):
            ekok *= i

            sayi1 //= i
            sayi2 //= i

        elif (sayi1 % i == 0 and sayi2 % i != 0):
            ekok *= i

            sayi1 //= i

        elif (sayi1 % i != 0 and sayi2 % i == 0):
            ekok *= i

            sayi2 //= i
        else:
            i += 1

        if (sayi1 == 1 and  sayi2 == 1):
            break
    return ekok

sayi1 = int(input("Sayı 1:"))
sayi2 = int(input("Sayı 2:"))

print ("EKOK:",ekok_bulma(sayi1,sayi2))
"""

"""
4.ALIŞTIRMA
Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın."
Örnek: 97 ---------> Doksan Yedi
"""
"""
birler = ["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

def okunus(sayi):

    birinci = sayi % 10
    ikinci = sayi // 10

    return onlar[ikinci] + " " + birler[birinci]

sayi = int(input("Bir Sayı Girin:"))

print(okunus(sayi))
"""

"""
5.ALIŞTIRMA
1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)
"""
"""
def pisagor_bulma():

    pisagor = list()

    for i in range(1,101):
        for j in range(1,101):

            c = (i ** 2 + j ** 2) ** 0.5

            if (c == int(c)):
                pisagor.append((i,j,int(c)))

    return pisagor

for i in pisagor_bulma():
    print(i)
"""

L = [4, 12, 2, 43, 15, 36]
L[2:4]
