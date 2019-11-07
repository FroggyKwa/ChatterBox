from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QComboBox
from gui import login, signup, edit, info


class ChatterBox(QMainWindow):
    def __init__(self):
        super().__init__()
        self.login_form = login.LoginForm(self)
        self.reg_form = signup.SignUpForm(self)
        self.edit_form = edit.EditForm(self)
        self.info_form = info.InfoForm(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(859, 600)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.messages_history_plain_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.messages_history_plain_text.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.messages_history_plain_text.setGeometry(QtCore.QRect(10, 30, 831, 441))
        self.messages_history_plain_text.setPlaceholderText("")
        self.messages_history_plain_text.setObjectName("messages_history_plain_text")

        self.messagebox_text_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.messagebox_text_edit.setGeometry(QtCore.QRect(10, 480, 831, 71))
        self.messagebox_text_edit.setObjectName("messagebox_text_edit")

        self.current_user_lbl = QtWidgets.QLabel(self.centralwidget)
        self.current_user_lbl.setGeometry(QtCore.QRect(390, 0, 441, 31))

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)

        self.current_user_lbl.setFont(font)
        self.current_user_lbl.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.current_user_lbl.setObjectName("current_user_lbl")

        self.online_label = QLabel(self)
        self.online_label.setText('Connection to server failed')
        self.online_label.setGeometry(650, 10, 200, 50)



        MainWindow.setCentralWidget(self.centralwidget)
        self.send_btn = QtWidgets.QPushButton(self.centralwidget)
        self.send_btn.move(750, 555)
        self.send_btn.setText('Send')
        self.send_btn.resize(self.send_btn.sizeHint())

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 859, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.login = self.menubar.addAction('Sign In')
        self.login.triggered.connect(self.open_login_form)

        self.reg = self.menubar.addAction('Sign Up')
        self.reg.triggered.connect(self.open_reg_form)

        self.edit = self.menubar.addAction('Edit')
        self.edit.setVisible(False)
        self.edit.triggered.connect(self.open_edit_form)

        self.info = self.menubar.addAction('Info')
        self.info.setVisible(False)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def open_login_form(self):
        self.login_form.show()
        self.login_form.setModal(True)

    def open_reg_form(self):
        self.reg_form.show()

    def open_edit_form(self):
        self.edit_form.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ChatterBox"))
        self.messagebox_text_edit.setPlaceholderText(_translate("", "Type your message here"))
        #self.menuLog_In.setTitle(_translate("MainWindow", "Log-In"))
        #self.menuSign_Up.setTitle(_translate("MainWindow", "Sign-Up"))
        #self.menuRegister.setTitle(_translate("MainWindow", "Register"))
