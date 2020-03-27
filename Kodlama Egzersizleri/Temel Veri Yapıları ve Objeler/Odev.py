""""
=> Problem 1
Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini format metoduyla yapmaya çalışın.
""" #=== Cevap : ===
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
carpim = int(a*b*c)
print("Birinci Sayi={}\nİkinci Sayi={}\nÜçüncü Sayi={}".format(a, b, c))
print("Sonuç=", carpim)

"""
=> Problem 2
Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.
Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)
#=== Cevap : ===\n"""
kilo = int(input("Kilo :"))
boy = int(input("Boy :"))
endeks: float = ((kilo) / ((boy*boy)/10000))
print("Vücut kitle indeksiniz : ", int(endeks))
if endeks <= 18.5:
    print("Cılızsın")
if endeks <= 24.9:
    print("Normalsin")
if endeks <= 29.9:
    print("Fazla kilolusun")
else:
    print("Aşırı Obezsin")
"""
=> Problem 3
Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini 
gerektiğini hesaplayın.
#=== Cevap : ===\n"""
#kilometede yaktığı * yapılan yol

yaktigi = float(input("Yaktığı :"))
kilometre = int(input("Kaç kilometre yapıldığı :"))
sonuc = float(yaktigi*kilometre)
print("Toplam ödemeniz gereken tutar ={} TL".format(float(sonuc)))

"""
=> Problem 4
Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.
"""
ad = str(input("Adınızı girtiniz :"))
soyad = str(input("Soyadınızı giriniz :"))
telefon = str(input("Telefon numaranızı giriniz :"))
print("Adınız :{}\nSoyadınız :{}\nNumaranız :{}", format(ad, telefon))

"""
=> Problem 5
Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.
"""

"""
=> Problem 6
Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.
Hipotenüs Formülü: a^2 + b^2 = c^2
"""

