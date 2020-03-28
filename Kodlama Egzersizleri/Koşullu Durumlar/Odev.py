"""Problem 1
Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.
 Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)
 BKİ 18.5'un altındaysa -------> Zayıf
 BKİ 18.5 ile 25 arasındaysa ------> Normal
 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu
 BKİ 30'un üstündeyse -------------> Obez
 *****************************************************************************"""
"""
kilo = float(input("Kilo: "))
boy = int(input("Boy(cm olarak giriniz: )"))
indeks = (kilo / (boy ** 2)*10000)
print("Beden Kitle İndeksiniz : {}".format(indeks))
if indeks <= 18.5:
    print("Zayıf")
elif indeks > 18.5 and indeks <= 25 :
    print("Normal")
elif indeks >25 and indeks <= 30:
    print("Fazla Kilolu")
else:
    print("Obez")
"""

"""Problem 2
Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.
*****************************************************************************"""
"""
sayi1 = int(input("1.sayi: "))
sayi2 = int(input("2.sayi: "))
sayi3 = int(input("3.sayi: "))
if sayi1 > sayi2 and sayi1 > sayi2:
    print("En Büyük Sayı 1.sayıdır.")
elif sayi2 > sayi1 and sayi2 > sayi3:
    print("En Büyük Sayı 2.sayıdır.")
else:
    print("En Büyük Sayı 3.sayıdır.")
"""
"""Problem 3
Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.
    Vize1 toplam notun %30'una etki edecek.
    Vize2 toplam notun %30'una etki edecek.
    Final toplam notun %40'ına etki edecek.

    Toplam Not >=  90 -----> AA
    Toplam Not >=  85 -----> BA
    Toplam Not >=  80 -----> BB
    Toplam Not >=  75 -----> CB
    Toplam Not >=  70 -----> CC
    Toplam Not >=  65 -----> DC
    Toplam Not >=  60 -----> DD
    Toplam Not >=  55 -----> FD
    Toplam Not <  55 -----> FF
*****************************************************************************"""
"""
vize1 = float(input("1.vize notunuzu giriniz: "))
vize2 = float(input("2.vize notunuzu giriniz: "))
final = float(input("Final notunuzu giriniz: "))
ortalama = (vize1*30/100) + (vize2*30/100) + (final*40/100)
if ortalama >= 90:
    print("AA")
elif ortalama >= 85:
    print("BA")
elif ortalama >= 80:
    print("BB")
elif ortalama >= 75:
    print("CB")
elif ortalama >= 70:
    print("CC")
elif ortalama >= 65:
    print("DC")
elif ortalama >= 60:
    print("DD")
elif ortalama >= 55:
    print("FD")
else:
    print("FF")
"""
"""Problem 4
Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.
Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi 
olduğunu bulmaya çalışın.
Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi 
olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın
Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.
Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz.
Kullanımı şu şekildedir ;
abs(-4)
4
abs(5)
5
*****************************************************************************"""
print("Hesaplamak istediğiniz şekli lütfen belirtiniz : ")
print("1- Üçgen")
print("2- Dörtgen")
secim = int(input("Lütfen bir seçim yapın : "))
if secim == 1:
    print("Lütfen Üçgen Kenarlarını Giriniz.")
    ucgenkenar1 = int(input("Lütfen Uzun kenar uzunluğunu giriniz : "))
    ucgenkenar2 = int(input("Lütfen Kısa kenar uzunluğunu giriniz : "))
    ucgenkenar3 = int(input("Lütfen Kısa kenar uzunluğunu giriniz : "))
    ucgenvecre = ucgenkenar1+ucgenkenar2+ucgenkenar3
    if ucgenkenar2+ucgenkenar3 < ucgenkenar1:
        print("İki kısa kenarın toplamı uzun kenara eşit yada büyük olmalıdır")
    elif ucgenkenar2 == ucgenkenar3:
        print("Bu bir ikizkenar üçgendir\nÜçgenin çevresinin toplamı : {}".format(ucgenvecre))
    elif ucgenkenar1 == ucgenkenar2 == ucgenkenar3:
        print("Bu bir üçüzkenar üçgendir.\nÜçgenin çevresinin toplamı : {}".format(ucgenvecre))
    else:
        print("Bu bir yamuk üçgendir.\nÜçgenin çevresinin toplamı : {}".format(ucgenvecre))
elif secim == 2:
    print("4 kenar uzunluğunu belirtin.")
    kenar1 = int(input("Lütfen 1.kenar uzunluğunu giriniz."))
    kenar2 = int(input("Lütfen 2.kenar uzunluğunu giriniz."))
    kenar3 = int(input("Lütfen 3.kenar uzunluğunu giriniz."))
    kenar4 = int(input("Lütfen 1.kenar uzunluğunu giriniz."))
    dikdortgencevre = kenar1+kenar2+kenar3+kenar4
    if kenar1 == kenar2 == kenar3 == kenar4:
        print("Bu bir karedir.\nKarenin çevresi : {}".format(kenar1*4))
    elif kenar1 == kenar2 and kenar3 == kenar4:
        print("Bu bir dikdörtgendir\nDikdörtgenin çevresi : {}".format(dikdortgencevre))
    elif kenar1 == kenar3 and kenar2 == kenar4:
        print("Bu bir dikdörtgendir\nDikdörtgenin çevresi : {}".format(dikdortgencevre))
    elif kenar1 == kenar4 and kenar2 == kenar3:
        print("Bu bir dikdörtgendir\nDikdörtgenin çevresi : {}".format(dikdortgencevre))
    else:
        print("Bir bir yamuk dörtgendir.\nYamuk dörtgenin çevresi : {}".format(dikdortgencevre))
else:
    print("Lütfen geçerli seçim yapın")

"""====DİPNOT : abs(Mutlak Değer Alma Fonksiyonu) ile çok uğraşmadım.Çünkü formülle fazla vakit öldürmek istemedim.Amaç if kullanımının pratiğini
yapmak olduğu için genel geçer formülden gittim.Ancak abs() kullanımı araştırıp öğrendim.
abs() bir işlemin mutlak değeri anlamına gelmektedir.Örneği a = | 3-5 | işleminin pozitif çıkmasını bekliyoruz.Çünkü mutlak değer.
Kullanımına basit bir örnek :
a = int(3-5)
print(abs(a)) 
Sonuç : 2"""
