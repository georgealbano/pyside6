from main_window import MainWindow, Info
from display import Display
from styles import setupTheme
from enviroments import WINDOW_ICON
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel


if __name__ == '__main__':

    app = QApplication()
    window = MainWindow()
    icon = QIcon(str(WINDOW_ICON))
    # tema
    setupTheme(app)

    # Info
    info = Info('45^2')
    window.addv_layout(info)

    # Display
    display = Display()
    window.addv_layout(display)

    window.adjust_fixed_size()

    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    window.show()
    app.exec()
