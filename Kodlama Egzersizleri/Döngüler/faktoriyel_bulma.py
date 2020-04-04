print("""
***************************
Faktöriyel Bulma Programı

Çıkmak için 'q' ya basınız
***************************
""")
#Algoritma => 5! = 5.4.3.2.1 => 5! = 5.4.3.2

while True:
     sayi = input("Sayı : ")
     if (sayi == "q"):
         print("Pragram Sonlandırılıyor....")
         break
     else:
         sayi = int(sayi)

         faktoriyel = 1

         for i in range(2, sayi+1):
             print("Faktöriyel ", faktoriyel, "i:", i)
             faktoriyel *= i
         print("Faktöriyel ", faktoriyel)