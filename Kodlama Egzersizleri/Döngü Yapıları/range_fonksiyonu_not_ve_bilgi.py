"""range() fonksiyonu : bu hazır fonksiyon bizim verdiğimiz değerlere göre range isimli bir ypaı oluşturur ve bu yapı listere oldukça benzer.Bu yapı
başlangıç,bitiş ve opsiyonel olarak artırma değeri alarak listelere benzeyen bir sayı dizisi oluşturur."""

range(0, 20)
print(*range(0, 20))
#range() fonksiyonunun ne oluşturuğunu görmek için başına * koymamız gerekir. print(*range(0, 20))
print(*range(0, 100))

print(*range(15))
#Not : Eğer başlangıç değeri vermezsek python bunu otomatik olarak alır ve 1den başlatır.

print(*range(1, 100, 2))
#Not : 1'den başka 100'e kadar git 2 atlayarak git
print(*range(5, 100, 3))

#Not : range() fonksiyonu her zaman atlayarak gider.Eğer sondan başa doğru gitmemiz gerkeiyorsa arttırma değerine -1 veriyoruz
print(*range(20, 0, -1))

for i in range(0, 101):
    print(i)

#Not : stringi i ile çarptırdık ve bir görsel oluşturduk.
for i in range(1, 10):
    print("*" * i)
