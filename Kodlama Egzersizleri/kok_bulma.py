"""""
2.dereceden bir bilinmeyenli denmklemin köklerini bulma
Denklem : ax^2 + bx + c

Delta  Hesaplama : b**2 - 4*a*c

Birinci Kök : (-b -delta **0.5)/ (2*a)
İkinci Kök : (-b + delta ** 0.5) / (2*a)
"""
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

delta = b ** 2 - 4 * a * b * c

x1 = (-b - delta ** 0.5) / (2 * a)
x2 = (-b + delta ** 0.5) / (2 * a)

print("Birinci kök : {}\nİkinci Kök : {} ".format(x1, x2))