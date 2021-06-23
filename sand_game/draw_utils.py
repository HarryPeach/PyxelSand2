from sand_game import canvas
import pyxel
from typing import Tuple


def draw_cursor(width: int, color: int, canvas_width: int, canvas_height: int,
                canvas_start_loc: Tuple[int, int]) -> None:
    """Draws the cursor

    Args:
        width (int): The width of the cursor
        color (int): The color to draw
        canvas_width (int): The width of the canvas
        canvas_height (int): The height of the canvas
        canvas_start_loc (tuple[int, int]): The starting location of the canvas
    """
    if ((pyxel.mouse_x < canvas_start_loc[0] - 1 or
            pyxel.mouse_x > canvas_start_loc[0] + canvas_width) or
            (pyxel.mouse_y < canvas_start_loc[1] - 1 or
                pyxel.mouse_y > canvas_start_loc[1] + canvas_height)):
        pyxel.mouse(True)
    else:
        pyxel.mouse(False)
        pyxel.circb(pyxel.mouse_x, pyxel.mouse_y, width, color)
