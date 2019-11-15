"""
5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
"""


LETTER1 = ord(input("буква 1: "))
LETTER2 = ord(input("буква 2: "))

print(f"буква 1 на: {LETTER1 - 96} место")
print(f"Вторая буква: {LETTER2 - 96} место")

if LETTER1 > LETTER2:
    print(f"между ними букв: {LETTER1 - LETTER2 - 1}")
else:
    print(f"между ними букв: {LETTER1 - LETTER2 - 1}")