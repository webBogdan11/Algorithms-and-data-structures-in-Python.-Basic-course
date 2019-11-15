# 2. Выполнить логические побитовые операции "И", "ИЛИ" и др.
# над числами 5 и 6. Выполнить
# над числом 5 побитовый сдвиг вправо и влево.


A = 5
print("Var 'А': ", A)

B = 6
print("Var 'В': ", B)

AND_RES = (A & B)
print("AND: ", AND_RES)

OR_RES = (A | B)
print("OR 'ИЛИ': ", OR_RES)

EX_OR_RESULT = (A ^ B)
print("NOT OR: ", EX_OR_RESULT)

BIT_LEFT_RES = A << 4
print("Сдвиг на 4 знака в лево числа 5: ", BIT_LEFT_RES)

BIT_RIGHT_RES = A >> 3
print("Сдвиг на 3 знака в право числа 5: ", BIT_RIGHT_RES)