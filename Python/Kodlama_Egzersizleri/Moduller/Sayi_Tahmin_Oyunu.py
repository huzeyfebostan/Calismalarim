import random
import time

print("""**************SAYI TAHMİN OYUNU**************""")

print("1 ile 100 arasında bir sayı girin")

rastgele_sayi = random.randint(1,100)
tahmin_hakki = 5

while True:

    tahmin = int(input("Sayi Girin:"))

    if (tahmin < rastgele_sayi):
        print(".......")
        time.sleep(0.3)

        print("Daha yüksek bir sayı girin")

        tahmin_hakki -= 1

    elif (tahmin > rastgele_sayi):
        print(".......")
        time.sleep(0.3)

        print("Daha küçük bir sayı girin")

        tahmin_hakki -= 1

    else:
        print(".......")
        time.sleep(0.3)

        print("Doğru tahmin ettiniz \nTahmininiz:{} \nRastgele Sayı:{}".format(tahmin,rastgele_sayi))
        break

    if (tahmin_hakki == 0):
        print("Tahmin hakkınız doldu doğru sayıyı tahmin edemediniz. \nSayı:{}".format(rastgele_sayi))
        break





















