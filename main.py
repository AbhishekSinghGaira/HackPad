import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D3, board.D4, board.D2, board.D1]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        # 1 → Copy (Ctrl + C)
        KC.MACRO(
            Press(KC.LCTRL),
            Tap(KC.C),
            Release(KC.LCTRL)
        ),

        # 2 → Paste (Ctrl + V)
        KC.MACRO(
            Press(KC.LCTRL),
            Tap(KC.V),
            Release(KC.LCTRL)
        ),

        # 3 → Quick Note (types date + note text)
        KC.MACRO(
            "---- Quick Note ----\n",
            "Date: ",
            "\n• "
        ),

        # 4 → Save + Switch App (Ctrl+S then Alt+Tab)
        KC.MACRO(
            Press(KC.LCTRL),
            Tap(KC.S),
            Release(KC.LCTRL),
            Press(KC.LALT),
            Tap(KC.TAB),
            Release(KC.LALT),
        ),
    ]
]

if __name__ == '__main__':
    keyboard.go()
