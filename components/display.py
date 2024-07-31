from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt
from components.utils import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUM_WIDTH


class Display(QLineEdit):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.config_style()

    def config_style(self):
        self.setStyleSheet('font-size: 50px')
        self.setMinimumHeight(BIG_FONT_SIZE)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[TEXT_MARGIN for _ in range(4)])
        self.setMinimumWidth(MINIMUM_WIDTH)
