from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys



app = QApplication(sys.argv)
screen = app.primaryScreen()
if screen:
    screenGeometry = screen.geometry()
    screen_width = screenGeometry.width()
    screen_height = screenGeometry.height()
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task manager app")
        self.resize(screen_width, screen_height)
app.setStyle('Fusion')
window = MainWindow()
layout = QVBoxLayout()
app.setStyleSheet("QLabel { margin: 1ex; }")



label8 = QLabel('8:00')
label16 = QLabel('16:00')
label00 = QLabel('00:00')
progressBar = QProgressBar()    
workButton = QPushButton('work mode')
planButton = QPushButton('plan mode')
viewButton = QPushButton('view your progress')
hSeparator = QFrame()
hSeparator.setFrameShape(QFrame.Shape.HLine)
hSeparator.setFrameShadow(QFrame.Shadow.Sunken)
hSeparator2 = QFrame()
hSeparator2.setFrameShape(QFrame.Shape.HLine)
hSeparator2.setFrameShadow(QFrame.Shadow.Sunken)


def workMode():
    alert = QMessageBox()
    alert.setText('You have been hacked!')
    alert.exec()
workButton.clicked.connect(workMode)
def planMode():
    alert = QMessageBox()
    alert.setText('You have been hacked again!')
    alert.exec()
planButton.clicked.connect(planMode)



layout.addWidget(workButton)
layout.addWidget(planButton)
layout.addWidget(viewButton)
layout.addWidget(hSeparator)
layout.addWidget(label8)
layout.addWidget(label16)
layout.addWidget(label00)
layout.addWidget(hSeparator2)
#layout.addWidget(progressBar)



window.setLayout(layout)
window.show()
app.exec()