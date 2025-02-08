import sys
from PyQt6.QtCore import QTimer, Qt, QDate, QTime
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, 
    QToolBar, QStatusBar, QLabel, QPushButton, 
    QProgressBar, QFrame, QMessageBox, QCalendarWidget
)

def mainWindow():
    screen_width, screen_height = 800, 600
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    if screen:
        screenGeometry = screen.geometry()
        screen_width = screenGeometry.width()
        screen_height = screenGeometry.height()
    app.setStyle('Fusion')
    app.setStyleSheet("QLabel { margin: 1ex; }")

    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Task manager app")
            self.resize(screen_width, screen_height)

            # Tworzenie głównego widgetu i layoutu
            self.central_widget = QWidget(self)
            self.setCentralWidget(self.central_widget)
            self.layout = QVBoxLayout(self.central_widget)

            # Tworzenie etykiety jako poruszający się element
            self.label = QLabel("🕒", self.central_widget)
            self.label.resize(40, 40)

            # Timer do aktualizacji pozycji co 100 ms
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.update_position)
            self.timer.start(100)

            self.update_position()  # Ustawienie początkowej pozycji

            # Toolbar
            toolbar = QToolBar("Toolbar", self)
            toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
            action1 = QAction(QIcon(), "Action1", self)
            action1.triggered.connect(self.action1_triggered)
            action2 = QAction(QIcon(), "Action2", self)
            action2.triggered.connect(self.action2_triggered)
            toolbar.addAction(action1)
            toolbar.addAction(action2)

            # Status bar i przyciski
            self.statusBar = QStatusBar(self)
            self.setStatusBar(self.statusBar)

            self.workButton = QPushButton('work mode')
            self.planButton = QPushButton('plan mode')
            self.viewButton = QPushButton('view your progress')

            # Separatory
            hSeparator = QFrame()
            hSeparator.setFrameShape(QFrame.Shape.HLine)
            hSeparator.setFrameShadow(QFrame.Shadow.Sunken)

            hSeparator2 = QFrame()
            hSeparator2.setFrameShape(QFrame.Shape.HLine)
            hSeparator2.setFrameShadow(QFrame.Shadow.Sunken)

            # Akcje dla przycisków
            self.workButton.clicked.connect(self.workMode)
            self.planButton.clicked.connect(self.planMode)
            self.viewButton.clicked.connect(self.viewCalendar)

            # Dodanie widgetów do layoutu
            self.layout.addWidget(toolbar)
            self.layout.addWidget(self.workButton)
            self.layout.addWidget(self.planButton)
            self.layout.addWidget(self.viewButton)
            self.layout.addWidget(hSeparator)
            self.layout.addWidget(hSeparator2)

        def update_position(self):
            """Aktualizuje pozycję elementu na podstawie aktualnego czasu."""
            current_time = QTime.currentTime()
            seconds = current_time.second()
            milliseconds = current_time.msec()

            # Przesuwanie elementu w zakresie 0-300 px w poziomie
            x_pos = (seconds * 5) % 300  # Sekundy wpływają na pozycję X
            y_pos = (milliseconds // 10) % 250  # Milisekundy wpływają na pozycję Y

            self.label.move(x_pos, y_pos)

        def workMode(self):
            alert = QMessageBox()
            alert.setText('You have been hacked!')
            alert.exec()

        def planMode(self):
            alert = QMessageBox()
            alert.setText('You have been hacked again!')
            alert.exec()

        def viewCalendar(self):
            """Przełącza widok na kalendarz."""
            # Czyści obecny layout
            for i in reversed(range(self.layout.count())):
                widget = self.layout.itemAt(i).widget()
                if widget is not None:
                    widget.setParent(None)

            # Tworzy nowy kalendarz
            self.calendar = QCalendarWidget()
            self.calendar.setGridVisible(True)
            self.calendar.clicked[QDate].connect(self.showDate)

            self.label = QLabel()
            self.exitBtn = QPushButton("Exit")
            self.exitBtn.clicked.connect(self.addDefaultWidgets)

            # Dodaje nowe widgety
            self.layout.addWidget(self.label)
            self.layout.addWidget(self.exitBtn)
            self.layout.addWidget(self.calendar)

        def showDate(self, date):
            self.label.setText(date.toString())

        def addDefaultWidgets(self):
            """Przywraca oryginalne widgety po zamknięciu kalendarza."""
            for i in reversed(range(self.layout.count())):
                widget = self.layout.itemAt(i).widget()
                if widget is not None:
                    widget.setParent(None)

            self.layout.addWidget(self.workButton)
            self.layout.addWidget(self.planButton)
            self.layout.addWidget(self.viewButton)

        def action1_triggered(self):
            alert = QMessageBox()
            alert.setText('You have been hacked1!')
            alert.exec()

        def action2_triggered(self):
            alert = QMessageBox()
            alert.setText('You have been hacked2!')
            alert.exec()

    window = MainWindow()
    window.show()
    app.exec()

mainWindow()
