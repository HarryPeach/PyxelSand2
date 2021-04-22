import pyxel


def draw_cursor(width: int, color: int) -> None:
    pyxel.circb(pyxel.mouse_x, pyxel.mouse_y, width, color)
