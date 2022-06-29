kolichestvo = input('Введите количество элементов списка - только цифрой!: ')

spisok = []
for i in range( 1, int(kolichestvo )+ 1):
    element = input('Введите значение для элемента списка - только цифрой: ')
    spisok.append(element)

spisok.sort()
print (' Заданный вами список: ',   spisok )

