"""
break ifadesi döngülerde programcıların en çok kullanılar ifadeleridir :
Döngü herhangi bir yerde ve herhangi bir zamanda break ifadesiyle karşılaştığı zamman çalışmasını durdurur.Böylelikle hiçbir koşula bağlı
kalmadan sonlamış olur.
Break ifadesi sadece de sadece içindeki bulunduğu döngüyü sonlandırır.Eğer iç içe döngüler bulunuyorsa ve en içteki döngüde break kullanılmışsa sadece
içteki döngü sona erer.

i = 0
while (i < 10):
    print("i : ", i)
    i += 1

i = 0
while (i < 10):
    if (i == 5):
        break
    print("i:", i)
    i += 1

liste = [1, 2, 3, 4, 5]
for i in liste:
    if (i == 3):
        break
    print("i:",i)

#while True: => eğer hiçbir yerde sonlandırma ifadesi kulklanılmazsa bu döngü sonsuza kadar gider.Ancak herhangi bir yerde break varsa döngü sonlanır.
while True:
    isim = input("İsim(Çıkmak için 'q' ya basın):")
    if (isim == "q"):
        print("Programdan çıkılıyor...")
        break
    print("İsminiz : ", isim)
"""
"""
continue ifadesi => continue ifadesi break'e göre biraz daha az kullanılan bir ifadedir.Anlamı şı şekildedir :
    Döngü herhangi bir yerde ve herhangi bir zamanda continue ifadesiyle karşılaştığı zaman geri kalan işlerini yapmadan bloğun başına döner.

liste = list(range(11))
print((liste))
for i in liste:
    print("i:", i)

liste = list(range(11))
print((liste))
for i in liste:
    if (i ==3 or i == 5):
        continue
    print("i:", i)

#sonsuz dögnü :
i = 0
while (i <10 ):
    if (i == 2):
        continue
    print(i)
    i += i
"""