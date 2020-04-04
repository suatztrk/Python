print("""
*************************
Kullanıcı Girişi Programı
*************************
""")

sys_kullanici_adi = "suat"
sys_parola = "123456"
giris_hakki = 3
while True:
    kullanici_adi=input("Kullanıcı Adı : ")
    parola=input("Parola : ")
    if (kullanici_adi != sys_kullanici_adi and parola==sys_parola):
        print("Kullanıcı Adı Hatalı")
        giris_hakki -= 1
        print("Kalan Giriş Hakkınız : ", giris_hakki)
    elif (kullanici_adi == sys_kullanici_adi and parola != sys_parola):
        print("Parola Hatalı")
        giris_hakki -= 1
        print("Kalan Giriş Hakkınız : ", giris_hakki)
    elif (kullanici_adi != sys_kullanici_adi and parola != sys_parola):
        print("Kullanıcı ve Parola Hatalı")
        giris_hakki -= 1
        print("Kalan Giriş Hakkınız : ", giris_hakki)
    else:
        print("Sisteme başarıyla giriş yapıldı.")
        break
    if (giris_hakki == 0):
        print("Giriş Hakkınız Bitti.....")
        break