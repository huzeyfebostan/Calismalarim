print("""
**************************************************
--------------KULLANICI GİRİŞ PANELİ--------------
**************************************************
""")

sys_kullanici_adi = "Hoze"
sys_parola = "12345"
giris_hakki = 3

while True:
    kullanici_adi = input("Kullanıcı Adı Girin:")
    parola = input ("Parolayı Girin:")
    if (sys_kullanici_adi != kullanici_adi and sys_parola == parola):
        print("Kullanıcı Adı Yanlış....")
        giris_hakki -= 1
        print("Kalan Giriş Hakkınız ", giris_hakki)
    elif (sys_kullanici_adi == kullanici_adi and sys_parola != parola):
        print("Parola Yanlış")
        print("Kalan Giriş Hakkınız ", giris_hakki)
        giris_hakki -= 1
    elif (sys_kullanici_adi != kullanici_adi and sys_parola != parola):
        print("Kullanıcı Adı ve Parola Yanlış")
        giris_hakki -=1
        print("Kalan Giriş Hakkınız ",giris_hakki)
    else:
        print("Sisteme Giriş Yapılıyor....")
        break
    if (giris_hakki == 0):
        print("Giriş Hakkınız Tükendi")
        break
