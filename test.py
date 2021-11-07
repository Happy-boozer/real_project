from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setStyleSheet('background-color: #DCDCDC') #
        Form.resize(116, 291)
        self.body_button = QtWidgets.QPushButton(Form)
        self.body_button.setStyleSheet('background-color: #F0E68C') #
        self.body_button.setGeometry(QtCore.QRect(20, 50, 93, 28))
        self.body_button.setObjectName("body_button")
        self.engine_button = QtWidgets.QPushButton(Form)
        self.engine_button.setStyleSheet('background-color: #228B22') #
        self.engine_button.setGeometry(QtCore.QRect(20, 120, 93, 28))
        self.engine_button.setObjectName("engine_button")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setStyleSheet('background-color: #5F9EA0')
        self.pushButton_3.setGeometry(QtCore.QRect(20, 200, 81, 28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.body_button.setText(_translate("Form", "кузова"))
        self.engine_button.setText(_translate("Form", "двигатея"))
        self.pushButton_3.setText(_translate("Form", "элктрики"))
#python -m PyQt5.uic.pyuic -x [FILENAME].ui -o [FILENAME].py

'''
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 342)
        Form.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.d_button = QtWidgets.QPushButton(Form)
        self.d_button.setGeometry(QtCore.QRect(70, 220, 93, 28))
        self.d_button.setObjectName("d_button")
        self.fixing_button = QtWidgets.QPushButton(Form)
        self.fixing_button.setGeometry(QtCore.QRect(200, 220, 93, 28))
        self.fixing_button.setAutoDefault(False)
        self.fixing_button.setDefault(False)
        self.fixing_button.setObjectName("fixing_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.d_button.setText(_translate("Form", "диагностика"))
        self.fixing_button.setText(_translate("Form", "Ремонт"))
'''

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


'''

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(572, 479)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(270, 30, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(270, 79, 121, 31))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(0, 20, 261, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 80, 261, 41))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(20, 190, 81, 51))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(260, 190, 91, 51))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(180, 190, 81, 51))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4 = QtWidgets.QComboBox(Form)
        self.comboBox_4.setGeometry(QtCore.QRect(370, 190, 121, 51))
        self.comboBox_4.setObjectName("comboBox_4")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 51, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(0, 260, 621, 221))
        self.label_4.setText("")
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setPixmap(QtGui.QPixmap(
            "Users/dev/Desktop/Porsche_911S_2.7L_1967.jpg.740x555_q85_box-129,0,1774,1232_crop_detail_upscale.jpg"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(290, 150, 61, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(390, 130, 161, 41))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(210, 160, 55, 16))
        self.label_7.setObjectName("label_7")
        self.comboBox_5 = QtWidgets.QComboBox(Form)
        self.comboBox_5.setGeometry(QtCore.QRect(100, 190, 73, 51))
        self.comboBox_5.setObjectName("comboBox_5")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(110, 160, 55, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(490, 60, 55, 16))
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(360, 20, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "ФИО"))
        self.label_2.setText(_translate("Form", "контактный телефон"))
        self.label_3.setText(_translate("Form", "марка"))
        self.label_5.setText(_translate("Form", "месяц"))
        self.label_6.setText(_translate("Form", "год"))
        self.label_7.setText(_translate("Form", "день"))
        self.label_8.setText(_translate("Form", "час"))
        self.label_9.setText(_translate("Form", "TextLabel"))
        self.pushButton.setText(_translate("Form", "PushButton"))


choise = ()
days = []
i = 1
while i != 32:
    days.append(i)
    i += 1

marks_list = ['Ford', 'Honda', 'Hyundai', 'Kia', 'Lada (ВАЗ)', 'Mazda', 'Mercedes-Benz', 'Mitsubishi', 'Nissan',
              'Skoda', 'Toyota', 'Volkswagen', 'Acura', 'Daihatsu', 'Datsun', 'Honda', 'Infiniti', 'Isuzu',
              'Lexus', 'Mazda', 'Mitsubishi', 'Scion', 'Subaru', 'Suzuki', 'Toyota', 'Buick', 'Chevrolet', 'Chrysler',
              'Dodge', 'Ford', 'GMC', 'Hummer', 'Jeep', 'Lincoln', 'Mercury', 'Oldsmobile', 'Pontiac', 'Aurus', 'ГАЗ',
              'Москвич', 'ТагАЗ', 'УАЗ', 'Audi', 'BMW', 'Opel', 'Porsche', 'Volkswagen',
              'Daewoo', 'Genesis',
              'Hyundai', 'Kia', 'SsangYong', 'Alfa Romeo', 'Aston Martin', 'Bentley', 'Bugatti', 'Citroen', 'DS',
              'Ferrari',
              'Fiat', 'Jaguar', 'Lamborghini', 'Lancia', 'Land Rover', 'Maserati', 'Maybach', 'Mini', 'Peugeot',
              'Ravon',
              'Renault', 'Rolls-Royce', 'Rover', 'Saab', 'SEAT', 'Skoda', 'Smart', 'Volvo', 'ZAZ', 'Brilliance', 'BYD',
              'Changan', 'Chery', 'DongFeng', 'FAW', 'Foton', 'GAC', 'Geely', 'Great Wall', 'Haima', 'Haval', 'JAC',
              'Lifan', 'Luxgen', 'Zotye']

monthes = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
           'September', 'October', 'November', 'December']


class MyFform(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()
        sys.exit(app.exec_())


class StartForm(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.fixing_button.clicked.connect(self.OnClick)

    def handleButton(self):
        self.dialog = MyFform()
        self.dialog.show()

    def OnClick(self):
        self.w1 = MyFform()
        self.w1.show()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication([])
    xe = StartForm()
    xe.show()
    sys.exit(app.exec())
'''