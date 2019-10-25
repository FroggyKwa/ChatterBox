from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow


class ChatterBox(QMainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(859, 588)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.messages_history_plain_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.messages_history_plain_text.setEnabled(False)
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 859, 21))
        self.menubar.setObjectName("menubar")
        self.menuLog_In = QtWidgets.QMenu(self.menubar)
        self.menuLog_In.setObjectName("menuLog_In")
        self.menuSign_Up = QtWidgets.QMenu(self.menubar)
        self.menuSign_Up.setObjectName("menuSign_Up")
        self.menuRegister = QtWidgets.QMenu(self.menubar)
        self.menuRegister.setObjectName("menuRegister")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuLog_In.menuAction())
        self.menubar.addAction(self.menuSign_Up.menuAction())
        self.menubar.addAction(self.menuRegister.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.messagebox_text_edit.setPlaceholderText(_translate("MainWindow", "Type your message here"))
        self.current_user_lbl.setText(_translate("MainWindow", "Username"))
        self.menuLog_In.setTitle(_translate("MainWindow", "Log-In"))
        self.menuSign_Up.setTitle(_translate("MainWindow", "Sign-Up"))
        self.menuRegister.setTitle(_translate("MainWindow", "Register"))
