import datetime
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtGui import QPixmap, QBitmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from datetime import time, date
from calendar import monthrange, month_name
import json
import os

monthes = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
           'September', 'October', 'November', 'December']
'''
record = {'YEAR': {2021: {1: None,
                          2: None,
                          3: None,
                          4: None,
                          5: None,
                          6: None,
                          7: None,
                          8: None,
                          9: None,
                          10: None,
                          11: None,
                          12: None
                          },
                   2022: {
                       1: None,
                       2: None,
                       3: None,
                       4: None,
                       5: None,
                       6: None,
                       7: None,
                       8: None,
                       9: None,
                       10: None,
                       11: None,
                       12: None
                   }}
        '''
'''
with open('base.txt', mode="w", encoding='utf-8') as f:
    json.dump(record, f)
    f.close()
'''

marks_list = ['Ford', 'Honda', 'Hyundai', 'Kia', 'Lada (ВАЗ)', 'Mazda', 'Mercedes-Benz', 'Mitsubishi', 'Nissan',
              'Renault', 'Skoda', 'Toyota', 'Volkswagen', 'Acura', 'Daihatsu', 'Datsun', 'Honda', 'Infiniti', 'Isuzu',
              'Lexus', 'Mazda', 'Mitsubishi', 'Scion', 'Subaru', 'Suzuki', 'Toyota', 'Buick', 'Chevrolet', 'Chrysler',
              'Dodge', 'Ford', 'GMC', 'Hummer', 'Jeep', 'Lincoln', 'Mercury', 'Oldsmobile', 'Pontiac', 'Aurus', 'ГАЗ',
              'Москвич', 'ТагАЗ', 'УАЗ', 'Audi', 'BMW', 'Mercedes-Benz', 'Opel', 'Porsche', 'Volkswagen',
              'Daewoo', 'Genesis',
              'Hyundai', 'Kia', 'SsangYong', 'Alfa Romeo', 'Aston Martin''Bentley', 'Bugatti', 'Citroen', 'DS',
              'Ferrari',
              'Fiat', 'Jaguar', 'Lamborghini', 'Lancia', 'Land Rover', 'Maserati', 'Maybach', 'Mini', 'Peugeot',
              'Ravon',
              'Renault', 'Rolls-Royce', 'Rover', 'Saab', 'SEAT', 'Skoda', 'Smart', 'Volvo', 'ZAZ', 'Brilliance', 'BYD',
              'Changan', 'Chery', 'DongFeng', 'FAW', 'Foton', 'GAC', 'Geely', 'Great Wall', 'Haima', 'Haval', 'JAC',
              'Lifan', 'Luxgen', 'Zotye']

hours_d = {10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0,
           17: 0, 18: 0}  # time for everything

monthes = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
           'September', 'October', 'November', 'December']
days = []
i = 1
while i != 32:
    days.append(i)
    i += 1
# rembo = record.copy()

'''
for k in record['YEAR']:
    for j in range(1, len(record['YEAR'][k]) + 1):
        special_days = {}
        for i in days:
            for l in range(monthrange(k, j)[0], monthrange(k, j)[1]):
                if i == l:
                    if date(k, j, i).weekday() in range(0, 5):
                        special_days[i] = hours_d

        record['YEAR'][k][date(k, j, l).strftime('%B')] = special_days

with open('base.txt', encoding='utf-8', mode='w') as f:
    json.dump(record, f)
    f.close()
'''


def checking(dicto):
    file_path = 'base.txt'
    with open('base.txt', encoding='utf-8', mode='r+') as f:
        a = str(dicto)
        if os.stat(file_path).st_size != 0:
            record = f.readlines()
            if record:
                print(type(record))
                a = str(dicto)
                for i in list(record):
                    print(type(i))
                    if a in i:
                        print(a)
                        print(i)
                        return False
                    else:
                        print(a)
                        print(i)
                        json.dump(a, f)
                        return True
        else:
            json.dump(a, f)
            return True


'''
if checking(('2021', '10', "17", '14')):
    print('j')
else:
    print('o')
#json.dump(record, f)
#f.close()
'в данном цикле происходит заполнение записи '


# проверка на принадлежность к рабочим дням
# print(days)
'''