#\n yazılan yerin geri kalan kısmını aşağıa atar
#\t bir tgab boşlöuğu kadar kalanının ardından boşluk bırakır
print("Merhaba\nNasılsın\nİyimisin ?")
print("Ocak\tŞubat\tMart")

#€type() => içine gönderdiğimiz değerin hangi tipte olduğunu söyler
print(type("Suat"))

#sep => araya istediğimiz karakterleri koyar işareti koyar
print(5,15,49,71)
print(5,15,49,71,sep="/")

#string değerin başına * koyulursa içerdeki değerin boşluklı yazılmasını sağlar
print(*"TBMM")
print(*"TBMM",sep=".")

#formatlama => formatla fonksiyonuyla yazdığımız değerleri süslü parantezler içerisine yerleştirmeye yarar ( https://pyformat.info/ )
print("")

#liste.append => verdiğimiz değeri lsiteye eklemimizi sağlar
liste[10,9,2,3,4,5]
list.append(23)
print(liste)

#liste.pop => son elemanı listeden atmaya yarar
#liste.pop(0) => elemanı kendimiz seçebiliriz.

liste = [23, 33, 62, 54, 89, 66, 32]
print(liste)

#liste.sort => elemanları küçükten büyüğe doğru sıralamak için kullanılır.
#liste.sort(reverse = true) => listeyi büyükten küçüğe sıralamak için kullanılır.

liste.sort()
print(liste)

liste.pop(0)
print(liste)

listee = [[1, 2], [3, 4], [5, 6]]
print(listee[1][0]) #listenin 1.elemanlarının 0.elemanını seçme

#demetlerin(tuple) sadece 2 tanne fonksiyonu bulunur
#count , index
#demetin içinde kaç tane 1 in geçtiğini gösterir
demet2= (1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 5, 6, 9, 8)
print(demet2.count(1))

#index => arattığımız şeyin varsa hangi index te bulunduğunu gösterir
#Not : Demetler sonradan değiştirilemez
