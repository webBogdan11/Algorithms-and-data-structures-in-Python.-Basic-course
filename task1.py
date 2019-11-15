"""
Подсчет
"""

NUMB = int(input('text your numb: '))

A = NUMB % 10
B = ((NUMB - A) // 10) % 10
C = (NUMB - (B * 10) - A) // 100

RESULT_SUM = A + B + C

print(RESULT_SUM)
