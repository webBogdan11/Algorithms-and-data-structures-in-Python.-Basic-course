"""
По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки
"""

X1 = int(input("Введите х точки А: "))
Y1 = int(input("Введите у точки А: "))

X2 = int(input("Введите х точки В: "))
Y2 = int(input("Введите у точки В: "))

K = (Y1 - Y2) // (X1 - X2)
B = Y1 - X1 * K

result = f'Уравнение прмяой у = {K}x + {B}'
print(result)