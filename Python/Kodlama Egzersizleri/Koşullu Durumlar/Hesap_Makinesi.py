print("""*************************
HESAP MAKİNESİ PROGRAMI

Toplama işlemi için = 1'e basın
Çıkarma işlemi için = 2'ye basın
Çarpma işlemi için = 3'e basın
Bölme işlemi için = 4'e basın

*************************""")

a = float(input("Birinci sayıyı girin:"))
b = float(input("İkinci sayıyı girin:"))
islem = int(input("Yapılacak işlemi girin:"))

if islem == 1:
    print("{} ile {} sayılaının toplamı {}".format(a,b,a+b))
elif islem == 2:
    print("{} ile {} sayılarının farkı  {}".format(a,b,a-b))
elif islem == 3:
    print("{} ile {} sayılarıının çarpımı {}".format(a,b,a*b))
elif islem == 4:
    print("{} ile {} sayılarının bölümü {}".format(a,b,a/b))
else:
    print("Yanlış işlem seçtiniz")