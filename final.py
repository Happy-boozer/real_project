
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setStyleSheet('background-color: #C0C0C0') #
        Form.resize(572, 479)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(270, 30, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(270, 79, 121, 31))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QLineEdit(Form)
        self.textBrowser.setReadOnly(False) #
        self.textBrowser.setStyleSheet('background-color:#F5FFFA')
        self.textBrowser.setGeometry(QtCore.QRect(0, 20, 261, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QLineEdit(Form)
        self.textBrowser_2.setReadOnly(False) #
        self.textBrowser_2.setStyleSheet('background-color:#F5FFFA')
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 80, 261, 41))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setStyleSheet('background-color: #32CD32') #
        self.comboBox.setGeometry(QtCore.QRect(20, 190, 81, 51))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setStyleSheet('background-color: #32CD32') #
        self.comboBox_2.setGeometry(QtCore.QRect(260, 190, 91, 51))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setStyleSheet('background-color: #32CD32') #
        self.comboBox_3.setGeometry(QtCore.QRect(180, 190, 81, 51))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4 = QtWidgets.QComboBox(Form)
        self.comboBox_4.setStyleSheet('background-color: #32CD32') #
        self.comboBox_4.setGeometry(QtCore.QRect(370, 190, 121, 51))
        self.comboBox_4.setObjectName("comboBox_4")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 51, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(0, 260, 621, 221))
        self.label_4.setText("")
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setPixmap(QtGui.QPixmap("Users/dev/Desktop/Porsche_911S_2.7L_1967.jpg.740x555_q85_box-129,0,1774,1232_crop_detail_upscale.jpg"))
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
        self.comboBox_5.setStyleSheet('background-color: #32CD32')
        self.comboBox_5.setGeometry(QtCore.QRect(100, 190, 73, 51))
        self.comboBox_5.setObjectName("comboBox_5")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(110, 160, 55, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(400, 80, 200, 80))
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setStyleSheet('background-color: #0000CD') #
        self.pushButton.setGeometry(QtCore.QRect(400, 40, 100, 30))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "ФИО"))
        self.label_2.setText(_translate("Form", "контактный телефон"))
        self.label_3.setText(_translate("Form", "марка"))
        self.label_5.setText(_translate("Form", "число"))
        self.label_6.setText(_translate("Form", "год"))
        self.label_7.setText(_translate("Form", "месяц"))
        self.label_8.setText(_translate("Form", "час"))
        self.label_9.setText(_translate("Form", ""))
        self.pushButton.setText(_translate("Form", "Регистрация"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())