kolichestvo = input('Введите количество элементов списка - только цифрой!: ')

spisok1 = []
for i in range( 1, int(kolichestvo )+ 1):
    element = input('Введите значение для элемента списка - только цифрой: ')
    spisok1.append(element)

vvod = input("Введите список цифр  через ',' , 'или ', ';' , 'или', '/': ").replace(',', ';').replace('/', ';').split(';')
spisok2 = list(vvod)

spisok3 = []
for n in spisok1:
    if not (n in spisok2):
        spisok3.append(n)

print ( 'Список 1: ', spisok1)
print ( 'Список 2: ', spisok2)
print ('Новый список: ', spisok3)

