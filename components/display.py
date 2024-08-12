from cgi import test
from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from components.utils import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUM_WIDTH, is_num_ordot, is_empyty


class Display(QLineEdit):
    enter_request = Signal()
    del_request = Signal()
    clear_request = Signal()
    inputPressed = Signal(str)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.config_style()
        self.setFocusPolicy(Qt.StrongFocus)

    def config_style(self):
        self.setStyleSheet('font-size: 50px')
        self.setMinimumHeight(BIG_FONT_SIZE)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[TEXT_MARGIN for _ in range(4)])
        self.setMinimumWidth(MINIMUM_WIDTH)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        is_enter = key in [KEYS.Key_Enter, KEYS.Key_Return]
        is_del = key in [KEYS.Key_Backspace, KEYS.Key_Delete]
        is_esc = key in [KEYS.Key_Escape, KEYS.Key_Return]

        if is_enter or text == '=':
            print('Pressionou Enter')
            self.enter_request.emit()
            return event.ignore()

        if is_del or text.lower() == 'd':
            print('Pressionou del')
            self.del_request.emit()
            return event.ignore()

        if is_esc or text.lower() == 'c':
            print('Pressionou esc')
            self.clear_request.emit()
            return event.ignore()

        if is_empyty(test):
            return event.ignore()

        if is_num_ordot(text):
            print('input pressionado', type(self).__name__)
            self.inputPressed .emit(text)
            return event.ignore()
