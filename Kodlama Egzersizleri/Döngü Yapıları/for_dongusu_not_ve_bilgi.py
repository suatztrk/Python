#in => içerde var mı ? Diye kontrol eder.Sonucu true yada false olarak döner
print(5 in [1, 2, 3, 4])
print(2 in [1, 2, 3, 4])
print('p' in 'python')

#For Döngüsü => listelerin,stringlerin ve sözlüklerim içinde dolaşmamızı sağlar.
#for eleman in veri_yapısı(liste,demet vs):
    #yapilacak_islemler

liste = [1, 2, 3, 4, 5, 6, 7]
for liste in liste:
    print(liste)
#===========================================

toplam = 0
liste = [1, 2, 3, 4, 5, 6, 7]
for liste in liste:
    toplam = toplam + liste
print(toplam)

toplam = 0
liste = [1, 2, 3, 4, 5, 6, 7]
for liste in liste:
    toplam = toplam + liste
    print("Liste : {} , Toplam : {}".format(liste, toplam))
print(toplam)

liste1 = [1, 2, 3, 4, 34, 54, 63, 78]
for eleman in liste1:
    if eleman % 2 == 0:
        print(eleman)
#=> NOT : " %2 " 2ye bölümünden kalanı bulmak için kullanılır.Ayrıca çift sayıları belirleyebiliriz.

s = "Python"
for i in s:
    print(i)

s = "Python"
for i in s:
    print(i*3)

demet = [1, 2, 3, 4, 5]
for a in demet:
    print(a)

liste3 = [(1, 2), (3, 4), (5, 6), (7, 8)]
for eleman in liste3:
    print(eleman)

liste3 = [(1, 2), (3, 4), (5, 6), (7, 8)]
for (i,j) in liste3:
    print("i: {}, j: {}".format(i, j))

liste4 = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]
for (i, j, k) in liste4:
    print(i, j, k)

liste5 = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]
for (i, j, k) in liste5:
    print(i * j * k)

#sözlüklerde dönmek
# Ufak Hatırlatma
sozluk = {"bir": 1, "iki": 2, "üç": 3, "dört": 4}
print(sozluk.keys()) #=> dict_keys(['bir', 'iki', 'üç', 'dört'])
print(sozluk.values()) #=> dict_values([1, 2, 3, 4])
print(sozluk.items()) #=> dict_items([('bir', 1), ('iki', 2), ('üç', 3), ('dört', 4)])

sozluk = {"bir": 1, "iki": 2, "üç": 3, "dört": 4}
for i in sozluk:
    print(i)

sozluk = {"bir": 1, "iki": 2, "üç": 3, "dört": 4}
for i in sozluk.values():
    print(i)

sozluk = {"bir": 1, "iki": 2, "üç": 3, "dört": 4}
for i, j in sozluk.items():
    print("Anahtar:", i, "Değer:", j)