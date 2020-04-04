#liste üretmek ve oluşturmak için pythonda bulunan çok pratik bir yöntem.
#Hatırlatma => Listeye biz eleman eklemek için list.append() kullanarak ekliyorduk.
#Uzun yolu aşağıdadır.
"""
liste1 =[1, 2, 3, 4, 5]
liste2 = list()
print("Liste 1 : ", liste1)
for i in liste1:
    liste2.append(i)
print("Liste 2 : ", liste2)

liste3 = [1, 2, 3, 4, 5]
liste4 = (i for i in liste3) #2.i listede dönüyor ve ilk i'de listemize atılıyor.

liste5 = [3, 4, 5]
liste6 = [i * 2 for i in liste5]
print(liste6)

liste7 = [(1, 2), (3, 4), (5, 6)]
liste8 = [i * j for i, j in liste7]
print(liste8)

s = "Python"
liste9 = [i * 3 for i in s]
print(liste9)

#Listenin içinde listeleri tek bir liste yapmak.Normal yapılış.
liste10 = [[1, 2, 3,], [4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15]]
liste11 = list()

for i in liste10:
    for x in i:
        liste11.append(x)
print(liste11)
"""
#Listenin içinde listeleri tek bir liste yapmak.Lis Comprehension yapılış.
liste12 = [[1, 2, 3,], [4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15]]
liste13 = [x for i in liste12 for x in i]
print((liste13))