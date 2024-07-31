from pathlib import Path
import re

ROOT_DIR = Path(__file__).parent
FILE_DIR = ROOT_DIR / 'files'
WINDOW_ICON = FILE_DIR / 'icon_app.png'
# print(WINDOW_ICON)


# color
PRIMARY_COLOR = '#1e81b0'
DARKER_PRIMARY_COLOR = '#16658a'
DARKEST_PRIMARY_COLOR = '#115270'

# Sizing
BIG_FONT_SIZE = 40
MEDIUM_FONT_SIZE = 24
SMALL_FONT_SIZE = 18
TEXT_MARGIN = 15
MINIMUM_WIDTH = 500


NUM_OR_DOT_REGEX = re.compile(r'[0-9.]')


def is_num_ordot(text: str):
    return bool(NUM_OR_DOT_REGEX.search(text))


def is_empyty(text: str):
    return text == ''
