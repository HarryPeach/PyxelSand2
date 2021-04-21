import pyxel


def draw_cursor(color: int) -> None:
    pyxel.rect(pyxel.mouse_x, pyxel.mouse_y - 1, 1, 1, color)
    pyxel.rect(pyxel.mouse_x, pyxel.mouse_y + 1, 1, 1, color)
    pyxel.rect(pyxel.mouse_x - 1, pyxel.mouse_y, 1, 1, color)
    pyxel.rect(pyxel.mouse_x + 1, pyxel.mouse_y, 1, 1, color)
