print("""
****************************
Kullanıcı Girişi
****************************
""")

bst_kullanıcı_adı = "Hoze"
bst_parola = "012345"

kullanıcı_adı = input("Kullanıcı Adını Girin:")
parola = input("Şifreyi Girin:")

if (bst_kullanıcı_adı != kullanıcı_adı and bst_parola != parola):
    print("Kullanıcı adı ve parola yanlış")
elif (bst_kullanıcı_adı == kullanıcı_adı and bst_parola != parola):
    print("Parola yanlış")
elif(bst_kullanıcı_adı != kullanıcı_adı and bst_parola == parola):
    print("Kullanıcı adı hatalı")
else:
    print("Sisteme başarıyla giriş yapıldı")