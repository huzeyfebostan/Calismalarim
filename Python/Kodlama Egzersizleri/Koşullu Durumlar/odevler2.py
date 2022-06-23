
print("""
*********************************
GEOMETRİ PROGRAMI
*********************************

Üçgen için 1'e 
Dikdörtgen için 2'ye basınız
""")

a = int(input("Giriş Yapın:"))

if (a==1):
    print("Üçgen Bölümünü Seçtiniz\n")
    u1 = int(input("Birinci kenarı girin:"))
    u2 = int(input("İkinci kenarı girin:"))
    u3 = int(input("Üçüncü kenarı girin:"))
    if (u1>0 and u2>0 and u3>0):
        if (u1 == u2 == u3):
            print("Kenarları girilen üçgenin türü EŞKENAR ÜÇGEN'dir")
        elif (u1 == u2 or u1 == u3 or u2 == u3):
            print("Kenarları girilen üçgenin türü İKİZKENAR ÜÇGEN'dir")
        elif (u1 != u2 and u1 != u3 and u2 != u3):
            print("Kenarları girilen üçgenin türü SIRADAN ÜÇGEN'dir")
    else:
        print("Girilen sayılar bir üçgen belirtmiyor")

elif (a==2):
    print("Dikdörtgen Bölümünü Seçtiniz\n")
    d1 = int(input("Birinci kenarı girin:"))
    d2 = int(input("İkinci kenarı girin:"))
    d3 = int(input("Üçüncü kenarı girin:"))
    d4 = int(input("Dördüncü kenarı girin:"))
    if (d1>0 and d2>0 and d3>0 and d4>0):
        if (d1 == d2 == d3 == d4):
            print("Kenarları girilen dörtgen KARE'dir")
        elif (d1 == d3 and d2 == d4):
            print("Kenarları girilen dörtgen DİKDÖRTGEN'dir")
        elif (d1 != d2 and d1 != d3 and d1 != d4 or d2 != d3 and d2 != d4 or d3 != d4):
            print("Kenarları girilen dörtgen SIRADAN DÖRTGEN'dir")
    else:
        print("Sıfırdan büyük bir kenar girin")
else:
    print("Girilen sayı ile ilgili bölüm bulunmamaktadır")
