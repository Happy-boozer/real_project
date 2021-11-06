import datetime
import erw
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtGui import QPixmap, QBitmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from datetime import time, date
from calendar import monthrange, month_name

'этот кусок  заполнял сам так как не смог придумать как всё сохранить так как я хочу'
record = {'YEAR': {2021: {
    10: {1: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
             17: 'unlocked', 18: 'unlocked'},
         4: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
             17: 'unlocked', 18: 'unlocked'},
         5: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
             17: 'unlocked', 18: 'unlocked'},
         6: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
             17: 'unlocked', 18: 'unlocked'},
         7: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
             17: 'unlocked', 18: 'unlocked'},
         8: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
             17: 'unlocked', 18: 'unlocked'},
         9: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
             17: 'unlocked', 18: 'unlocked'},
         12: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
              17: 'unlocked', 18: 'unlocked'},
         13: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
              17: 'unlocked', 18: 'unlocked'},
         14: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
              17: 'unlocked', 18: 'unlocked'},
         15: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
              17: 'unlocked', 18: 'unlocked'},
         16: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
              17: 'unlocked', 18: 'unlocked'},
         19: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
              17: 'unlocked', 18: 'unlocked'},
         20: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
              17: 'unlocked', 18: 'unlocked'},
         21: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
              17: 'unlocked', 18: 'unlocked'},
         22: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
              17: 'unlocked', 18: 'unlocked'},
         23: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
              17: 'unlocked', 18: 'unlocked'},
         25: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
              17: 'unlocked', 18: 'unlocked'},
         26: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
              17: 'unlocked', 18: 'unlocked'},
         27: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
              17: 'unlocked', 18: 'unlocked'},
         28: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
              17: 'unlocked', 18: 'unlocked'},
         29: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
              17: 'unlocked', 18: 'unlocked'}},
    11: {1: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
             17: 'unlocked', 18: 'unlocked'},
         2: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
             17: 'unlocked', 18: 'unlocked'},
         3: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
             17: 'unlocked', 18: 'unlocked'},
         4: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
             17: 'unlocked', 18: 'unlocked'},
         5: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
             17: 'unlocked', 18: 'unlocked'},
         8: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
             17: 'unlocked', 18: 'unlocked'},
         9: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
             17: 'unlocked', 18: 'unlocked'},
         10: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
              17: 'unlocked', 18: 'unlocked'},
         11: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
              17: 'unlocked', 18: 'unlocked'},
         12: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
              17: 'unlocked', 18: 'unlocked'},
         15: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
              17: 'unlocked', 18: 'unlocked'},
         16: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
              17: 'unlocked', 18: 'unlocked'},
         17: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
              17: 'unlocked', 18: 'unlocked'},
         18: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
              17: 'unlocked', 18: 'unlocked'},
         19: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
              17: 'unlocked', 18: 'unlocked'},
         22: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
              17: 'unlocked', 18: 'unlocked'},
         23: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
              17: 'unlocked', 18: 'unlocked'},
         24: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
              17: 'unlocked', 18: 'unlocked'},
         25: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
              17: 'unlocked', 18: 'unlocked'},
         26: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
              17: 'unlocked', 18: 'unlocked'},
         29: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
              17: 'unlocked', 18: 'unlocked'},
         30: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
              17: 'unlocked', 18: 'unlocked'}},
    12: {1: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
             17: 'unlocked', 18: 'unlocked'},
         2: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
             17: 'unlocked', 18: 'unlocked'},
         3: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
             17: 'unlocked', 18: 'unlocked'}},
    6: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
        17: 'unlocked', 18: 'unlocked'},
    7: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
        17: 'unlocked', 18: 'unlocked'},
    8: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
        17: 'unlocked', 18: 'unlocked'},
    9: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
        17: 'unlocked', 18: 'unlocked'},
    10: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
         17: 'unlocked', 18: 'unlocked'},
    13: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
         17: 'unlocked', 18: 'unlocked'},
    14: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
         17: 'unlocked', 18: 'unlocked'},
    15: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
         17: 'unlocked', 18: 'unlocked'},
    16: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
         17: 'unlocked', 18: 'unlocked'},
    17: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
         17: 'unlocked', 18: 'unlocked'},
    20: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
         17: 'unlocked', 18: 'unlocked'},
    21: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
         17: 'unlocked', 18: 'unlocked'},
    22: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
         17: 'unlocked', 18: 'unlocked'},
    23: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
         17: 'unlocked', 18: 'unlocked'},
    24: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
         17: 'unlocked', 18: 'unlocked'},
    27: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
         17: 'unlocked', 18: 'unlocked'},
    28: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
         17: 'unlocked', 18: 'unlocked'},
    29: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
         17: 'unlocked', 18: 'unlocked'},
    30: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
         17: 'unlocked', 18: 'unlocked'}},
    2022: {
        1: {10: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
                 17: 'unlocked', 18: 'unlocked'},
            11: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
                 17: 'unlocked', 18: 'unlocked'},
            12: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
                 17: 'unlocked', 18: 'unlocked'},
            13: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
                 17: 'unlocked', 18: 'unlocked'},
            14: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
                 17: 'unlocked', 18: 'unlocked'},
            17: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
                 17: 'unlocked', 18: 'unlocked'},
            18: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
                 17: 'unlocked', 18: 'unlocked'},
            19: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
                 17: 'unlocked', 18: 'unlocked'},
            20: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
                 17: 'unlocked', 18: 'unlocked'},
            21: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
                 17: 'unlocked', 18: 'unlocked'},
            24: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
                 17: 'unlocked', 18: 'unlocked'},
            25: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
                 17: 'unlocked', 18: 'unlocked'},
            26: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
                 17: 'unlocked', 18: 'unlocked'},
            27: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
                 17: 'unlocked', 18: 'unlocked'},
            28: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
                 17: 'unlocked', 18: 'unlocked'},
            31: {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
                 17: 'unlocked', 18: 'unlocked'}},
        'February': None,
        'March': None,
        'April': None,
        'May': None,
        'June': None,
        'July': None,
        'August': None,
        'September': None,
        'October': None,
        'November': None,
        'December': None
    }}}
# with open('base.txt', encoding='utf-8') as f:

'''
def changing(choice):
    choise = choice
    record['YEAR'][choise['date'][0]][choise['date'][1]][choise['date'][2]] = 'locked'
    record.update()

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

hours_d = {10: 'unlocked', 11: 'unlocked', 12: 'unlocked', 13: 'unlocked', 14: 'unlocked', 15: 'unlocked',
           17: 'unlocked', 18: 'unlocked'}  # time for everything

monthes = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
           'September', 'October', 'November', 'December']
days = []
i = 1
while i != 32:
    days.append(i)
    i += 1
# rembo = record.copy()

class Kill(QtWidgets.QMainWindow, erw.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Form = QtWidgets.QWidget()
        self.Form.show()
        self.d_button.clicked.connect(self.handleButton)
    def handleButton(self):


for k in record['YEAR']:
    for j in range(1, len(record['YEAR'][k]) + 1):
        special_days = {}
        for i in days:
            for l in range(monthrange(k, j)[0], monthrange(k, j)[1]):
                if i == l:
                    if date(k, j, i).weekday() in range(0, 5):
                        special_days[i] = hours_d

        record['YEAR'][k][date(k, j, l).strftime('%B')] = special_days
'в данном цикле происходит заполнение записи на весь ближний диапозон' 
'где подразумевается, что вся запись пуста'

print(record)

def cheking(prorramm.choise):
    pass

'''


# проверка на принадлежность к рабочим дням
# print(days)


class Fixing:
    # if weekday.date(2021, month, day) in weekdayes:

    pass


class Body(Fixing):
    pass


class Electric(Fixing):
    pass


class locksmith(Fixing):
    pass


class Diagnostic:
    pass


class wheels(Diagnostic):
    pass


class AfterDTP(Diagnostic):
    pass


class suspension(Diagnostic):
    pass


'''

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Kill()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

'''
