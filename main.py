from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys

app = QApplication(sys.argv)
app.setStyle('Fusion')

window = QWidget()
layout = QVBoxLayout()
app.setStyleSheet("QLabel { margin: 1ex; }")

button = QPushButton('Button')
label = QLabel('Label')
progressBar = QProgressBar()    

def on_btn_clicked():
    alert = QMessageBox()
    alert.setText('You have been hacked!')
    alert.exec()
button.clicked.connect(on_btn_clicked)

layout.addWidget(button)
layout.addWidget(label)
layout.addWidget(progressBar)

window.setLayout(layout)
window.show()
app.exec()