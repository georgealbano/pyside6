
from components.utils import WINDOW_ICON, SMALL_FONT_SIZE
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        # Config basic layout
        self.cw = QWidget()
        self.v_layout = QVBoxLayout()
        self.cw.setLayout(self.v_layout)
        self.setCentralWidget(self.cw)

        # title window
        self.setWindowTitle('Meu titulo ')

        # ajust window
    def adjust_fixed_size(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

        # definindo um metodo para adicionar widgets nos layouts
    def widget_for_vlayout(self, widget: QWidget):
        self.v_layout.addWidget(widget)


class Info(QLabel):
    def __init__(
            self, text: str, parent: QWidget | None = None
    ) -> None:
        super().__init__(text, parent)
        self.confg_style()

    def confg_style(self):
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
