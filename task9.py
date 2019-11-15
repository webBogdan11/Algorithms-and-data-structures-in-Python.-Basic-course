# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

NMB_1 = int(input('Введите первое число: '))    # 5 4 3
NMB_2 = int(input('Введите второе число: '))    # 4 5 5
NMB_3 = int(input('Введите третье число: '))    # 3 3 4

if NMB_1 > NMB_2:
    if NMB_1 < NMB_3:
        print(f'{NMB_1} - is middle')

    else:
        print(f'{NMB_2} - is middle')

elif NMB_2 > NMB_3:
    if NMB_3 > NMB_1:
        print(f'{NMB_3} - is middle')
    else:
        print(f'{NMB_1} - is middle')

else:
    print(f'{NMB_2} - is middle')