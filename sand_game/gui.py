from __future__ import annotations
from typing import Callable, TYPE_CHECKING
if TYPE_CHECKING:
    from sand_game.__main__ import SandGame
import pyxel

# TODO (Harry): Add docstrings


class TexturedButton():
    def __init__(self, action: Callable, x: int, y: int, u: int, v: int, width: int,
                 height: int, enabled: bool = False):
        self.action = action
        self.x = x
        self.y = y
        self.u = u
        self.v = v
        self.width = width
        self.height = height
        self.enabled = enabled

    def set_enabled(self, enabled: bool) -> None:
        self.enabled = enabled


class Label():
    def __init__(self, value: str, x: int, y: int, color: int):
        self.value = value
        self.x = x
        self.y = y
        self.color = color

    def set_value(self, value: str) -> None:
        self.value = value

# def draw_menu(instance, start_x: int, start_y: int):
#     pyxel.text(start_x, start_y, "PEN SIZE", 7)
#     pyxel.blt(start_x, start_y + 8, 0, 5, 0, 5, 5)
#     pyxel.text(start_x + 8, start_y + 8, str(instance.pen_size), 7)
#     pyxel.blt(start_x + 14, start_y + 8, 0, 0, 0, 5, 5)


class Gui():

    def __init__(self, start_x: int, start_y: int) -> None:
        self.start_x = start_x
        self.start_y = start_y
        self.texts: list[Label] = []
        self.buttons: list[TexturedButton] = []

    def draw(self) -> None:
        self._draw_buttons()
        self._draw_texts()

    def _draw_texts(self) -> None:
        for text in self.texts:
            pyxel.text(self.start_x + text.x, self.start_y + text.y,
                       text.value, text.color)

    def _draw_buttons(self) -> None:
        for button in self.buttons:
            if not button.enabled:
                pyxel.blt(self.start_x + button.x, self.start_y + button.y, 0, button.u,
                          button.v, button.width, button.height)
            else:
                pyxel.blt(self.start_x + button.x, self.start_y + button.y, 0, button.u + 16,
                          button.v, button.width, button.height)

    def add_button(self, button: TexturedButton) -> None:
        self.buttons.append(button)

    def add_text(self, text: Label) -> None:
        self.texts.append(text)

    def handle_click(self, x: int, y: int):
        for button in self.buttons:
            start_x: int = button.x + self.start_x
            start_y: int = button.y + self.start_y
            if (x > start_x) and (x < start_x + button.width) and (y > start_y) and (y < start_y + button.height):
                button.action()
