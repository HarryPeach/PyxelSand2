import pyxel


def draw_cursor(width: int, color: int) -> None:
    pyxel.circb(pyxel.mouse_x, pyxel.mouse_y, width, color)
    # pyxel.rect(pyxel.mouse_x, pyxel.mouse_y - 1, 1, 1, color)
    # pyxel.rect(pyxel.mouse_x, pyxel.mouse_y + 1, 1, 1, color)
    # pyxel.rect(pyxel.mouse_x - 1, pyxel.mouse_y, 1, 1, color)
    # pyxel.rect(pyxel.mouse_x + 1, pyxel.mouse_y, 1, 1, color)
