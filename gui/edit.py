from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QPushButton, QLineEdit, QLabel


class EditForm(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.initUI(self)

    def initUI(self, EditForm):
        EditForm.setObjectName("EditForm")
        EditForm.resize(639, 442)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.label = QtWidgets.QLabel(EditForm)
        self.label.setGeometry(QtCore.QRect(30, 30, 47, 13))
        self.label.setObjectName("label")

        self.login_ln = QtWidgets.QLineEdit(EditForm)
        self.login_ln.setGeometry(QtCore.QRect(30, 50, 113, 20))
        self.login_ln.setObjectName("login_ln")
        self.login_error_label = QLabel(self)
        self.login_error_label.move(150, 55)

        self.password_ln = QtWidgets.QLineEdit(EditForm)
        self.password_ln.setGeometry(QtCore.QRect(30, 110, 113, 20))
        self.password_ln.setEchoMode(QLineEdit.Password)
        self.password_ln.setObjectName("password_ln")
        self.password_error_label = QLabel(self)
        self.password_error_label.move(150, 115)

        self.label_2 = QtWidgets.QLabel(EditForm)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 47, 13))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(EditForm)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 47, 13))
        self.label_3.setObjectName("label_3")

        self.country_ln = QtWidgets.QLineEdit(EditForm)
        self.country_ln.setGeometry(QtCore.QRect(30, 170, 113, 20))
        self.country_ln.setObjectName("country_ln")

        self.phone_ln = QtWidgets.QLineEdit(EditForm)
        self.phone_ln.setGeometry(QtCore.QRect(30, 230, 113, 20))
        self.phone_ln.setObjectName("phone_ln")
        self.phone_error_label = QLabel(self)
        self.phone_error_label.move(150, 235)

        self.website_ln = QtWidgets.QLineEdit(EditForm)
        self.website_ln.setGeometry(QtCore.QRect(30, 290, 113, 20))
        self.website_ln.setObjectName("website_ln")

        self.author_ln = QtWidgets.QLineEdit(EditForm)
        self.author_ln.setGeometry(QtCore.QRect(30, 350, 113, 20))
        self.author_ln.setObjectName("author_ln")

        self.label_4 = QtWidgets.QLabel(EditForm)
        self.label_4.setGeometry(QtCore.QRect(30, 330, 131, 16))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(EditForm)
        self.label_5.setGeometry(QtCore.QRect(30, 210, 91, 16))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(EditForm)
        self.label_6.setGeometry(QtCore.QRect(30, 270, 47, 13))
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(EditForm)
        self.label_7.setGeometry(QtCore.QRect(290, 140, 281, 16))
        self.label_7.setObjectName("label_7")

        self.quote_plain_text = QtWidgets.QPlainTextEdit(EditForm)
        self.quote_plain_text.setGeometry(QtCore.QRect(290, 170, 301, 201))
        self.quote_plain_text.setObjectName("quote_plain_text")

        self.submit_btn = QPushButton(self)
        self.submit_btn.setText('Save')
        self.submit_btn.move(550, 410)

        self.retranslateUi(EditForm)
        QtCore.QMetaObject.connectSlotsByName(EditForm)

    def retranslateUi(self, EditForm):
        _translate = QtCore.QCoreApplication.translate
        EditForm.setWindowTitle(_translate("EditForm", "Dialog"))
        self.label.setText(_translate("EditForm", "Login"))
        self.label_2.setText(_translate("EditForm", "Password"))
        self.label_3.setText(_translate("EditForm", "Country"))
        self.label_4.setText(_translate("EditForm", "Favourite book author"))
        self.label_5.setText(_translate("EditForm", "Phone number"))
        self.label_6.setText(_translate("EditForm", "Website"))
        self.label_7.setText(_translate("EditForm", "Favourite qoute"))
