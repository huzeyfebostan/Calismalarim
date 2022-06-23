print("""
****************************************

FAKTORİYEL HESAPLAMA PROGRAMI


çıkmak için 'q'ya basın
****************************************
""")

while True:
    sayi = input("Sayı girin:")

    if (sayi == "q"):
        print("Program'dan çıkılıyor")
        break

    else:
        sayi = int(sayi)
        faktoriyel = 1

        for i in range(2,sayi+1):
            faktoriyel *= i
            print("Faktoriyel",faktoriyel)

