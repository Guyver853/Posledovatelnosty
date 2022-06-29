vvod = input("Введите список цифр через ',' , 'или ', ';' , 'или', '/': ").replace(',', ';').replace('/', ';').split(';')
spisok = list(vvod)

uniq_spisok = list(set(spisok))
print('Результат: ', uniq_spisok)
