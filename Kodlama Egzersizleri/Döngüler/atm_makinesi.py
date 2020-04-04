print("""
***************************
Atm Makinesine Hoşgeldiniz

İşlemler :

1-) Bakiye Sorgulama
2-) Para Yatırma
3-) Para Çekme

Programdan Çıkmak İçin 'q' ya basın
***************************
""")
bakiye = 1000
while True:
    islem = input("İşlemi Seçiniz : ")
    if (islem == "q"):
        print("Yine Bekleriz....")
        break
    elif (islem == "1"):
        print("Bakiyeniz : {} TL'dir".format(bakiye))
    elif (islem == "2"):
        print("Bakiyeniz : {} TL dir".format(bakiye))
        miktar = int(input("Miktarını Giriniz : "))
        bakiye += miktar
        print("Yeni Bakiyeniz : {} TL dir".format(bakiye))
    elif (islem == "3"):
        print("Bakiyeniz : {} TL dir".format(bakiye))
        miktar = int(input("Miktarı Giriniz : "))
        if (bakiye - miktar <0):
            print("Bakiyenizden Fazla Tutar Çekemezsiniz....")
            continue
        bakiye -= miktar
        print("Yeni Bakiyeniz : {} TL dir".format(bakiye))
    else:
        print("Geçersiz İşlem....")