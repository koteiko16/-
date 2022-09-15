from math import*
from decimal import*

massiv = ['Сложение','Вычитание','Умножение','Деление','Возведение в степень','Логарифм','Округление в большую сторону','Округление в меньшую сторону']
print('Введите функцию:',*massiv,sep = '\n')

print()
func = input()

print('\nВведите первый элемент')
while True:
    a=input()
    if a.isdigit() or (a.count('.')==1 and a[0]!='.'):
        a = float(a)
        break
    else:
        print('Введенный элемент не является числом')

if func not in ['Округление в большую сторону','Округление в меньшую сторону']:
    print('\nВведите второй элемент')    
    while True:
        b=input()
        if b.isdigit() or (b.count('.')==1 and b[0]!='.'):
            b = float(b)
            break
        else:
            print('Введенный элемент не является числом')    
print()
if func=='Сложение':
    print(a+b)
elif func=='Умножение':
    print(a*b)
elif func=='Вычитание':
    print(a-b)
elif func=='Деление':
    print(a/b)
elif func=='Возведение в степень':
    print(a**b)
elif func=='Умножение':
    print(a*b)
elif func=='Логарифм':
    print(log(b)/log(a))
elif func=='Округление в большую сторону':
    n = int(input('Введите N = '))
    if round(a,n)<a:
        print(Decimal(str(round(a,n)))+Decimal(str(10**(-n))))
    else:
        print(round(a,n))
elif func=='Округление в меньшую сторону':
    n = int(input('Введите N = '))
    if round(a,n)>a:
        print(Decimal(str(round(a,n)))-Decimal(str(10**(-n))))
    else:
        print(round(a,n))