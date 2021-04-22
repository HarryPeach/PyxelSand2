from __future__ import annotations
from typing import Callable, TYPE_CHECKING
if TYPE_CHECKING:
    from sand_game.__main__ import SandGame
import pyxel


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
            pyxel.blt(self.start_x + button.x, self.start_y + button.y, 0, button.u,
                      button.v, button.width, button.height)

    def add_button(self, button: TexturedButton) -> None:
        self.buttons.append(button)

    # def handle_click(x: int, y: int):
    #     pass
