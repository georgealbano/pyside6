
from components.display import Display
from components.utils import MEDIUM_FONT_SIZE, is_num_ordot, is_empyty, is_valid_numb
from generic_windows import Info, MainWindow
from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import QPushButton, QGridLayout, QWidget
import math


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config_style()
        self.setFocusPolicy(Qt.NoFocus)

    def config_style(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)
        # self.setProperty('cssClass', 'specialButton')


class Button_grid(QGridLayout):
    def __init__(self, display: Display, info: Info, window: MainWindow,  *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self.display = display
        self.info = info
        self.window = window
        self._equation = ''
        self._equationInitialValue = 'Sua conta'
        self._left = None
        self._right = None
        self._op = None

        self.equation = self._equationInitialValue
        self.make_grid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def temporario(self):
        print('estou acessando o enter')

    def make_grid(self):
        self.display.enter_request.connect(
            self.temporario)

        self.display.del_request.connect(self.display.backspace)

        self.display.clear_request.connect(
            lambda: print('sinal recebido'))

        for i, row_data in enumerate(self._grid_mask):
            for j, button_tex in enumerate(row_data):
                button = Button(button_tex)

                if not is_num_ordot(button_tex) and not is_empyty(button_tex):
                    button.setProperty('cssClass', 'specialButton')
                    self._config_specialbutton(button)

                self.addWidget(button, i, j)
                slot = self.make_slot(
                    self._insert_button_todisplay,
                    button_tex
                )
                self._signal_clicked(button, slot)

    def _signal_clicked(self, button, slot):
        button.clicked.connect(slot)

    def _config_specialbutton(self, button):
        text = button.text()

        if text == 'C':

            self._signal_clicked(button, self._clear)

        if text in '+-/*':

            self._signal_clicked(
                button,
                self.make_slot(self._operator_clicked, button))

        if text == '=':

            self._signal_clicked(button, self._eq)

        if text == '^':

            self._signal_clicked(
                button,
                self.make_slot(self._operator_clicked, button))

        if text == '◀':
            self._signal_clicked(button, self.display.backspace)

    def make_slot(self, func, *args, **kwargs):
        @ Slot(bool)
        def real_slot(checked):
            func(*args, **kwargs)
        return real_slot

    def _insert_button_todisplay(self, button_text):

        new_display_text = self.display.text() + button_text

        if not is_valid_numb(new_display_text):
            return
        self.display.insert(button_text)

    def _operator_clicked(self, button):
        button_text = button.text()  # +-/* (etc...)
        display_text = self.display.text()  # Deverá ser meu número _left
        self.display.clear()  # Limpa o display

        # Se a pessoa clicou no operador sem
        # configurar qualquer número
        if not is_valid_numb(display_text) and self._left is None:
            self._show_erro('Não tem nada para colocar no valor da esquerda')
            return

        # Se houver algo no número da esquerda,
        # não fazemos nada. Aguardaremos o número da direita.
        if self._left is None:
            self._left = float(display_text)

        self._op = button_text
        self.equation = f'{self._left} {self._op} ??'

    def _eq(self):
        display_text = self.display.text()

        if not is_valid_numb(display_text):
            print('digite um numero valido')
            return
        self._right = float(display_text)
        self.equation = f'{self._left} {self._op} {self._right}'
        result = 'error'
        try:
            if '^' in self.equation and isinstance(self._left, float):
                result = math.pow(self._left, self._right)
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            print('Zero Division Error')

        except OverflowError:
            print('Numero ecedeu os limites ')

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self._left = result
        self._right = None

        if result == 'error':
            left = None

    def _show_erro(self, text):
        msg_box = self.window.make_msg_box()
        msg_box.setText(text)
        msg_box.setIcon(msg_box.Icon.Information)
        msg_box.exec()

    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue
        self.display.clear()
