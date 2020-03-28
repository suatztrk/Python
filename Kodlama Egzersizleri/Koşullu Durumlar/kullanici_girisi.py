print(""""*************************
Kullanıcı Girşi
*************************
""")

sys_kullanici_adi = "suat"
sys_parola = "123456"

kullanici_adi = input("Kullanıcı Adı: ")
parola = input("Parola: ")

if (kullanici_adi == sys_kullanici_adi and sys_parola == parola):
    print("Giriş Başarılı")
else :
    print("Giriş Başarısız")