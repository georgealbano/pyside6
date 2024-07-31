
from components.buttons import Button, Button_grid
from components.display import Display
from components.utils import WINDOW_ICON
from generic_windows import MainWindow, Info
from styles import setupTheme
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication


if __name__ == '__main__':

    app = QApplication()
    window = MainWindow()
    icon = QIcon(str(WINDOW_ICON))
    # tema
    setupTheme(app)

    # Info
    info = Info('45^2')
    window.widget_for_vlayout(info)

    # Display
    display = Display()
    window.widget_for_vlayout(display)

    # button
    button_grid = Button_grid(display)
    window.v_layout.addLayout(button_grid)

    window.adjust_fixed_size()
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    window.show()
    app.exec()
