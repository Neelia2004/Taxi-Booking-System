# importing sys
import sys

# importing the needed components
from PyQt6 import QtCore, QtGui, QtWidgets
import welcome

# responsible for running the application and waiting for things to happen
app = QtWidgets.QApplication(sys.argv)

w1 = welcome.WelcomePage(QtWidgets.QDialog())
w1.showing()
sys.exit(app.exec())
