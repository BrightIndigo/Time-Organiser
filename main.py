from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import *

app = QApplication([])
app.setStyle('Fusion')
palette = QPalette()
palette.setColor(QPalette.ButtonText, Qt.red)
app.setPalette(palette)
window = QWidget()
layout = QVBoxLayout()
app.setStyleSheet("QPushButton { margin: 5ex; } QLabel { margin: 5ex; }")

layout.addWidget(QProgressBar())
layout.addWidget(QLabel('Label'))
layout.addWidget(QPushButton('Button'))
window.setLayout(layout)

window.show()
app.exec_()