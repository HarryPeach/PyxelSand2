from __future__ import annotations
from typing import Callable, TYPE_CHECKING
if TYPE_CHECKING:
    from sand_game.__main__ import SandGame
import pyxel

# TODO (Harry): Add docstrings


class TexturedButton():
    def __init__(self, action: Callable, x: int, y: int, u: int, v: int, width: int,
                 height: int):
        self.action = action
        self.x = x
        self.y = y
        self.u = u
        self.v = v
        self.width = width
        self.height = height
        self.clicked = False

# def draw_menu(instance, start_x: int, start_y: int):
#     pyxel.text(start_x, start_y, "PEN SIZE", 7)
#     pyxel.blt(start_x, start_y + 8, 0, 5, 0, 5, 5)
#     pyxel.text(start_x + 8, start_y + 8, str(instance.pen_size), 7)
#     pyxel.blt(start_x + 14, start_y + 8, 0, 0, 0, 5, 5)

#     pyxel.text(start_x, start_y + 18, "PARTICLE", 7)
#     pyxel.blt(start_x, start_y + 26, 0, 16, 5, 15, 5)
    # pyxel.blt(start_x + 18, start_y + 26, 0, 0, 10, 15, 5)


class Gui():

    def __init__(self, start_x: int, start_y: int) -> None:
        self.start_x = start_x
        self.start_y = start_y
        self.buttons: list[TexturedButton] = []

    def draw(self) -> None:
        self._draw_buttons()

    def _draw_buttons(self) -> None:
        for button in self.buttons:
            if not button.clicked:
                pyxel.blt(self.start_x + button.x, self.start_y + button.y, 0, button.u,
                          button.v, button.width, button.height)
            else:
                pyxel.blt(self.start_x + button.x, self.start_y + button.y, 0, button.u + 16,
                          button.v, button.width, button.height)
            button.clicked = False

    def add_button(self, button: TexturedButton) -> None:
        self.buttons.append(button)

    def handle_click(self, x: int, y: int):
        for button in self.buttons:
            start_x: int = button.x + self.start_x
            start_y: int = button.y + self.start_y
            if (x > start_x) and (x < start_x + button.width) and (y > start_y) and (y < start_y + button.height):
                button.clicked = True
                button.action()
