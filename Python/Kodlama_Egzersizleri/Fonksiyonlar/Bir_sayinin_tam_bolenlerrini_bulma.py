print("""
***************************************************
BİR SAYININ TAM BÖLENLERİNİ BULAN PROGRAM
***************************************************
PROGRAMDAN ÇIKMAK İÇİN "q" TUŞUNA BASIN
***************************************************
""")

def bolenbulma(sayi):
    tam_bolenler = []

    for i in range(2,sayi):
        if (sayi % i == 0):
            tam_bolenler.append(i)
    return tam_bolenler

while True:
    sayi = input("Bir sayı girin:")

    if (sayi == "q"):
        print("Program Sonlandırılıyor...")
        break
    else:
        sayi = int(sayi)
        print("Tam Sayı Bölenler:",bolenbulma(sayi))