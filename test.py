from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QCalendarWidget, QLabel, QPushButton, QMessageBox
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.calendar_window()
        
    def calendar_window(self):
        layout = QVBoxLayout(self)
        
        # Calendar widget
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        self.calendar.clicked.connect(self.showDate)
        layout.addWidget(self.calendar)
        
        # Label to display selected date
        self.label = QLabel(self)
        date = self.calendar.selectedDate()
        self.label.setText(date.toString())
        layout.addWidget(self.label)
        
        # Button to trigger an action
        self.button = QPushButton("Show Selected Date", self)
        self.button.clicked.connect(self.showMessageBox)
        layout.addWidget(self.button)
        
        # Window settings
        self.setLayout(layout)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("Calendar")
        self.show()
        
    def showDate(self, date):
        self.label.setText(date.toString())

    def showMessageBox(self):
        selected_date = self.calendar.selectedDate().toString()
        QMessageBox.information(self, "Selected Date", f"You selected: {selected_date}")

def main():
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec())

main()
