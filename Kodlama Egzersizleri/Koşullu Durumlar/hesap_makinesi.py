print("""*********************
Hesap Makinesi Programı

İşlemler ;
1- Toplama İşlmei
2- Çıkarma İşlemi
3- Çarpma İşlemi
4- Bölme İşlemi
**********************""")
sayi1 = int(input("Birinci Sayı :"))
sayi2 = int(input("İkinci Sayı :"))
islem = input("İşlemi Giriniz : ")

if islem == "1":
    print("{} ile {} toplamı = {} sayısına eşittir ".format(sayi1, sayi2, sayi1 + sayi2))
elif islem == "2":
    print("{} ile {} çıkarılması = {} sayısına eşittir ".format(sayi1, sayi2, sayi1 - sayi2))
elif islem == "3":
    print("{} ile {} çarpımı = {} sayısına eşittir ".format(sayi1, sayi2, sayi1 * sayi2))
elif islem == "4":
    print("{} ile {} bölümü = {} sayısına eşittir ".format(sayi1, sayi2, float(sayi1 / sayi2)))
else:
    print("Geçerli Bir İşlem giriniz... :(")