from PyQt6 import QtCore, QtGui, QtWidgets
import UI
import sys

class admin_login_window(object):


    def __int__(self, Word):
        self.Word = QtWidgets.QDialog()
        self.start_administration_login(self.Word)

    def showing(self):
        self.Word.show()

    def closing(self):
        self.Word.close()

    def admin_button_clicked(self):
        print("Admin")

    def back_button_clicked(self):
        self.Word = QtWidgets.QDialog
        mainPage = UI.Taxi_Main_Page_Ui(QtWidgets.QDialog())
        mainPage.showing()
        self.closing()

    def start_administration_login(self, mainAdminPage):
        mainAdminPage.setObjectName("mainAdminPage")
        mainAdminPage.resize(400, 500)
        self.styling = QtWidgets.QGraphicsView(mainAdminPage)
        self.styling.setGeometry(QtCore.QRect(0, 0, 400, 500))
        self.styling.setStyleSheet("background-color: rgb(48, 116, 115);")
        self.styling.setObjectName("styling")
        self.administration_login_label = QtWidgets.QLabel(mainAdminPage)
        self.administration_login_label.setGeometry(QtCore.QRect(30, 20, 351, 101))
        fontstyle = QtGui.QFont()
        fontstyle.setFamily("ShellSansExpert")
        fontstyle.setPointSize(48)
        fontstyle.setBold(True)
        fontstyle.setWeight(75)
        self.administration_login_label.setFont(fontstyle)
        self.administration_login_label.setAutoFillBackground(False)
        self.administration_login_label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.administration_login_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.administration_login_label.setWordWrap(True)
        self.administration_login_label.setObjectName("administration_login_label")

        self.administration_login_button = QtWidgets.QPushButton(mainAdminPage, clicked=lambda: self.admin_button_clicked())
        self.administration_login_button.setGeometry(QtCore.QRect(150, 330, 113, 32))
        fontstyle = QtGui.QFont()
        fontstyle.setFamily("STIX Two Text")
        fontstyle.setPointSize(18)
        self.administration_login_button.setFont(fontstyle)
        self.administration_login_button.setStyleSheet("border-radius: 25px;\n"
                                                       "border: 2px solid #73AD21;\n"
                                                       "background-color: rgb(74, 74, 74);\n"
                                                       "color: rgb(255, 255, 255);\n"
                                                       "border-color: rgb(4, 4, 4);")
        self.administration_login_button.setObjectName("administration_login_button")
        self.password_information = QtWidgets.QLineEdit(mainAdminPage)
        self.password_information.setGeometry(QtCore.QRect(110, 270, 200, 20))
        self.password_information.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.password_information.setObjectName("pass_Txt")
        self.emailLabel = QtWidgets.QLabel(mainAdminPage)
        self.emailLabel.setGeometry(QtCore.QRect(110, 180, 80, 30))
        self.emailLabel.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                             "color: rgb(56, 56, 56);")
        self.emailLabel.setObjectName("email_information")
        self.passwordLabel= QtWidgets.QLabel(mainAdminPage)
        self.passwordLabel.setGeometry(QtCore.QRect(120, 240, 80, 30))
        self.passwordLabel.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                    "color: rgb(56, 56, 56);\n")

        self.passwordLabel.setObjectName("passwordLabel")
        self.email_Information = QtWidgets.QLineEdit(mainAdminPage)
        self.email_Information.setGeometry(QtCore.QRect(110, 210, 200, 20))
        self.email_Information.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.email_Information.setObjectName("email_Information")

        self.forget_password_button = QtWidgets.QPushButton(mainAdminPage)
        self.forget_password_button.setGeometry(QtCore.QRect(110, 380, 200, 30))
        font = QtGui.QFont()
        font.setFamily("STIX Two Text")
        font.setPointSize(18)
        self.forget_password_button.setFont(font)
        self.forget_password_button.setStyleSheet("border-radius: 25px;\n"
                                           "border: 2px solid #73AD21;\n"
                                           "background-color: rgb(74, 74, 74);\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "border-color: rgb(4, 4, 4);")

        self.forget_password_button.setObjectName("forget_password_button")

        self.Back_Button = QtWidgets.QPushButton(mainAdminPage, clicked=lambda: self.back_button_clicked())
        self.Back_Button.setGeometry(QtCore.QRect(10, 460, 100, 30))
        fontstyle = QtGui.QFont()
        fontstyle.setFamily("MS Shell Dlg 2")
        fontstyle.setPointSize(16)
        fontstyle.setBold(False)
        fontstyle.setItalic(False)
        fontstyle.setWeight(9)
        self.Back_Button.setFont(font)
        self.Back_Button.setStyleSheet("border-radius: 65px;\n"
                                           "font: 75 16pt \"MS Shell Dlg 2\";\n"
                                           "border: 2px solid #73AD21;\n"
                                           "background-color: rgb(74, 74, 74);\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "border-color: rgb(4, 4, 4);")

        self.Back_Button.setObjectName("forget_pass_Btn_2")
        self.retranslateUi(mainAdminPage)
        QtCore.QMetaObject.connectSlotsByName(mainAdminPage)

    def retranslateUi(self, mainAdminPage):
        update = QtCore.QCoreApplication.translate

        mainAdminPage.setWindowTitle(update("mainFrame", "Dialog"))
        self.administration_login_label.setText(update("mainFrame", "<html><head/><body><p><span style =\" font-size:20pt;\">Admin Login</span></p></body></html>"))
        self.administration_login_button.setText(update("mainFrame", "Login"))
        self.emailLabel.setText(update("mainFrame", "<html><head/><body><p><span style =\" font-weight:600; color:#ffffff;\">Username</span></p></body></html>"))
        self.passwordLabel.setText(update("mainFrame", "<html><head/><body><p><span style =\" font-weight:600; color:#ffffff;\">Password</span></p></body></html>"))
        self.forget_password_button.setText(update("mainFrame", "Forget Password"))
        self.Back_Button.setText(update("mainFrame", "Go Back"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainFrame = QtWidgets.QDialog()
    ui = admin_login_window()
    mainFrame.show()
    sys.exit(app.exec())



















