print("""
*****************************
ASAL SAYI BULMA PROGRAMI
*****************************
program'dan çıkmak için 'q'ya basın
""")

def asal_sayi(sayi):
    if (sayi == 1):
        return False
    elif (sayi == 2):
        return True
    else:
        for i in range(2,sayi):
            if (sayi % 2 == 0):
                return False
        return True

while True:
    sayi = input("Bir sayı girin:")

    if (sayi == 'q'):
        print("Progamdan çıkılıyor...")
        break
    else:
        sayi = int(sayi)
        if (asal_sayi(sayi)):
            print("{} sayısı asal sayıdır.".format(sayi))
        else:
            print("{} sayısı asal sayı değildir.".format(sayi))