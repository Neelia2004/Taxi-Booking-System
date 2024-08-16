# importing the needed components
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
import customerlogin
class WelcomePage:
    def __init__(self, word):  # creating the constructor
        print("Welcome page is running")
        self.word = word
        self.welcome_startui(self.word)

    def showing(self):
        self.word.show()

    def closing(self):
        self.word.close()

    def current_user_button_click(self):
        self.word = QtWidgets.QDialog()
        w2 = customerlogin.Customer_login(self.word)
        w2.showing()
        self.closing()

    def newuser_buttonclick(self):
        self.Word = QtWidgets.QDialog()
        # w3 = Window3_Page(self.Word)
        # w3.showing()
        self.closing()  # closes window 1

    def welcome_startui(self, welcome_page):
        print("In the Welcome Page, setup the ui")
        welcome_page.setObjectName("Welcome_page")
        welcome_page.resize(512, 300)

        fontstyle = QtGui.QFont()
        fontstyle.setWeight(QtGui.QFont.Weight.Bold)
        fontstyle.setBold(True)
        fontstyle.setPointSize(12)
        welcome_page.setFont(fontstyle)

        self.welcome_widget = QtWidgets.QWidget(welcome_page)
        self.welcome_widget.setGeometry(QtCore.QRect(0, 0, 512, 300))
        self.welcome_widget.setFont(fontstyle)
        self.welcome_widget.setObjectName("Welcome Widget")
        self.welcome_widget.setStyleSheet("background-color: rgb(106, 90, 205);")

        self.welcome_label = QtWidgets.QLabel(self.welcome_widget)
        self.welcome_label.setGeometry(QtCore.QRect(35, 20, 450, 40))
        fontstyle.setPointSize(16)
        self.welcome_label.setFont(fontstyle)
        self.welcome_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.welcome_label.setObjectName("Welcome_Label")

        self.newuser_button = QtWidgets.QPushButton(self.welcome_widget)
        self.newuser_button.setGeometry(QtCore.QRect(70, 200, 121, 51))
        fontstyle.setPointSize(8)
        fontstyle.setUnderline(True)
        self.newuser_button.setFont(fontstyle)
        self.newuser_button.setObjectName("newuser_button")
        self.newuser_button.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(0, 0, 0);")
        self.newuser_button.clicked.connect(self.newuser_buttonclick)


        self.currentuser_button = QtWidgets.QPushButton(self.welcome_widget)
        self.currentuser_button.setGeometry(QtCore.QRect(300, 200, 120, 51))
        fontstyle.setPointSize(8)
        fontstyle.setUnderline(True)
        self.currentuser_button.setFont(fontstyle)
        self.currentuser_button.setObjectName("Currentuser_button")
        self.currentuser_button.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(0, 0, 0);")  # White color for text
        self.currentuser_button.clicked.connect(self.current_user_button_click)

        self.welcome_label2 = QtWidgets.QLabel(self.welcome_widget)
        self.welcome_label2.setGeometry(QtCore.QRect(140, 80, 300, 50))
        fontstyle.setPointSize(12)
        fontstyle.setUnderline(True)
        self.welcome_label2.setFont(fontstyle)
        self.welcome_label2.setStyleSheet("color: rgb(255, 255, 255);")
        self.welcome_label2.setObjectName("welcome_label2")

        self.welcome_label3 = QtWidgets.QLabel(self.welcome_widget)
        self.welcome_label3.setGeometry(QtCore.QRect(100, 150, 100, 50))
        fontstyle.setPointSize(12)
        fontstyle.setUnderline(True)
        self.welcome_label3.setFont(fontstyle)
        self.welcome_label3.setStyleSheet("color: rgb(255, 255, 255);")
        self.welcome_label3.setObjectName("welcome_label3")

        self.welcome_label4 = QtWidgets.QLabel(self.welcome_widget)
        self.welcome_label4.setGeometry(QtCore.QRect(330, 150, 100, 50))
        fontstyle.setPointSize(12)
        fontstyle.setUnderline(True)
        self.welcome_label4.setFont(fontstyle)
        self.welcome_label4.setStyleSheet("color: rgb(255, 255, 255);")
        self.welcome_label4.setObjectName("welcome_label4")

        self.taxi_driver_button = QtWidgets.QPushButton(self.welcome_widget)
        self.taxi_driver_button.setGeometry(QtCore.QRect(81, 1, 80, 30))
        fontstyle.setPointSize(8)
        fontstyle.setUnderline(True)
        self.taxi_driver_button.setFont(fontstyle)
        self.taxi_driver_button.setObjectName("taxi_driver_button")


        self.administration_button = QtWidgets.QPushButton(self.welcome_widget)
        self.administration_button.setGeometry(QtCore.QRect(1, 1, 80, 30))
        fontstyle.setPointSize(8)
        fontstyle.setUnderline(True)
        self.administration_button.setFont(fontstyle)
        self.administration_button.setObjectName("administration_button")

    def update(self, welcome_page):
        update_text = QtCore.QCoreApplication.translate
        self.word.setWindowTitle(update_text("Welcome_page", "Login/ Registration Window"))
        self.word.setToolTip(update_text("Welcome_page", "Existing or New Customers"))
        self.welcome_label.setText(update_text("Welcome_page", "Online Taxi Booking System"))
        self.currentuser_button.setText(update_text("Welcome_page", "Login"))
        self.welcome_label2.setText(update_text("Welcome_page", "Welcome In!"))
        self.newuser_button.setText(update_text("Welcome_page", "Sign Up"))
        self.welcome_label3.setText(update_text("Welcome_page", "Register"))
        self.welcome_label4.setText(update_text("Welcome_page", "Sign In"))
        self.administration_button.setText(update_text("Welcome_page", "Administrator Login"))
        self.taxi_driver_button.setText(update_text("Welcome_page", "Taxi Driver Login"))
