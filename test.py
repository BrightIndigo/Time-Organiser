from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys
import datetime

class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.calendar_window()
        
    def calendar_window(self):
        layout =  QVBoxLayout(self)
        
        #calendar widget
        calendar = QCalendarWidget(self)
        calendar.setGridVisible(True)
        calendar.clicked[QDate].connect(self.showDate)
        layout.addWidget(calendar)
        
        #label
        self.label = QLabel(self)
        date = calendar.selectedDate()
        self.label.setText(date.toString())
        layout.addWidget(self.label)
        
        #layout
        self.setLayout(layout)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("Calendar")
        self.show()
        
    def showDate(self, date):
        self.label.setText(date.toString())
        
        
def main():
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec())

main()
        
        
        