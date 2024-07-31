from components.display import Display
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QPushButton, QGridLayout, QWidget

from components.utils import MEDIUM_FONT_SIZE, is_num_ordot, is_empyty


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config_style()

    def config_style(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)
        # self.setProperty('cssClass', 'specialButton')


class Button_grid(QGridLayout):
    def __init__(self, display: Display, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self.dispalay = display
        self.make_grid()

    def make_grid(self):
        for i, row_data in enumerate(self._grid_mask):
            for j, button_tex in enumerate(row_data):
                button = Button(button_tex)

                if not is_num_ordot(button_tex) and not is_empyty(button_tex):
                    button.setProperty('cssClass', 'specialButton')

                self.addWidget(button, i, j)
                button_slot = self.button_clicked(
                    self._insert_button_todisplay,
                    button
                )
                button.clicked.connect(button_slot)

    def button_clicked(self, func, *args, **kwargs):
        @Slot(bool)
        def real_slot(checked):
            func(*args, **kwargs)
        return real_slot

    def _insert_button_todisplay(self, button):
        button_text = button.text()
        self.dispalay.insert(button_text)
