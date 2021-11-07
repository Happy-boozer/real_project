from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setStyleSheet('background-color: #DCDCDC')
        Form.resize(400, 342)
        Form.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.d_button = QtWidgets.QPushButton(Form)
        self.d_button.setStyleSheet('background-color: #3CB371') #
        self.d_button.setGeometry(QtCore.QRect(70, 220, 93, 28))
        self.d_button.setObjectName("d_button")
        self.fixing_button = QtWidgets.QPushButton(Form)
        self.fixing_button.setStyleSheet('background-color: #008B8B') #
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())