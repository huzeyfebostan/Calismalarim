print("""
******************************************************

ATM PROGRAMINA HOŞ GELDİNİZ

İŞLEMLER;

Bakiye Sorgulama için 1'e

Para Yatırma için 2'ye

Para Çekmek için 3'e

Çıkmak İçin 'q'ya basınız

******************************************************

""")

bakiye = 1000

while True:
    islem = input("İşlem Seçiniz:")

    if (islem == "q"):
        print("Tekrar Bekleriz")
        break

    elif (islem == "1"):
        print("Bakiyeniz {} tl dir".format(bakiye))

    elif (islem == "2"):
        miktar = int(input("Yastırılacak miktarı giriniz:"))
        print("Yatırılan miktar",miktar)
        bakiye += miktar
        print("Güncel bakiye",bakiye)

    elif (islem =="3"):
        miktar = int(input("Çekilecek miktarı giriniz:"))
        print("Çekilecek miktar",miktar)
        if (bakiye - miktar < 0):
             print("Yetersiz bakiye")
             continue
        bakiye -= miktar
        print("Güncel bakiye",bakiye)

else:
    print("Yanlış tuşu tuşladınız. Lütfen tekrar deneyiniz")