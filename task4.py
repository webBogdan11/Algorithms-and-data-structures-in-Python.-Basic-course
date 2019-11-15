"""
4. Написать программу, которая генерирует в указанных пользователем границах:
случайное целое число;
случайное вещественное число;
случайный символ.
"""


from random import random


INT_LIMIT_LEFT = int(input("Минимальная граница генерации целого числа с лева: "))
INT_LIMIT_RIGHT = int(input("Максимальная граница генерации целого числа с права: "))
INT_NUMB_RANDOM = int(random() * (INT_LIMIT_RIGHT - INT_LIMIT_LEFT + 1)) + INT_LIMIT_LEFT
print(INT_NUMB_RANDOM)

FLT_LEFT = int(input("Минимальная граница генерации дробного числа: "))
FLT_RIGHT = int(input("Максимальная граница генерации дробного числа: "))
FLT_NUMB = random() * (FLT_RIGHT - FLT_LEFT) + FLT_LEFT
print(round(FLT_NUMB, 3))

STR_LEFT = ord(input("Минимальная граница: "))
STR_RIGHT = ord(input("Максимальная граница: "))
STR_NUMB = int(random() * (STR_RIGHT - STR_LEFT + 1)) + STR_LEFT
print(chr(STR_NUMB))