from datetime import time, date

record = {'YEAR': {2020: {'January': None,
                            'February': None,
                            'March': None,
                            'April': None,
                            'May': None,
                            'June': None,
                            'July': None,
                            'August':None,
                            'September':None,
                            'October':None,
                            'November':None,
                            'December':None,},
                2021: {'January': None,
                            'February':None,
                            'March':None,
                            'April':   None,

                            'May':None,
                            'June':None,
                            'July':None,
                            'August':None,
                            'September':None,
                            'October':None,
                            'November': None,
                            'December': None
                                }}}




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

hours_d = [time(11), time(13), time(15), time(17)]  # time for diagnostic

hours_F = [time(10), time(12), time(14), time(16), time(18)]  # time for fixing

weekdayes = ['monday', 'tuesday', 'wendsday', 'thursday', 'friday']  # weekdays

monthes = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
           'September', 'October', 'November', 'December']
days = []
i = 1
while i != 32:
    days.append(i)
    i += 1
special_days = {}
#if date()
#проверка на принадлежность к рабочим дням
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
