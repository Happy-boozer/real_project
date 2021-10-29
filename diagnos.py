from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(116, 300)
        self.WH = QtWidgets.QPushButton(Form)
        self.WH.setGeometry(QtCore.QRect(10, 20, 93, 28))
        self.WH.setObjectName("WH")
        self.DTP = QtWidgets.QPushButton(Form)
        self.DTP.setGeometry(QtCore.QRect(10, 90, 81, 28))
        self.DTP.setObjectName("DTP")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 200, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.WH.setText(_translate("Form", "проверка УК"))
        self.DTP.setText(_translate("Form", "трпосле ДТП"))
        self.pushButton_3.setText(_translate("Form", "Подвески"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())