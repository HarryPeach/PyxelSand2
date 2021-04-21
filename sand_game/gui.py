import pyxel


def draw_menu(instance, start_x: int, start_y: int):
    pyxel.text(start_x, start_y, "PEN SIZE", 7)
    pyxel.blt(start_x, start_y + 8, 0, 5, 0, 5, 5)
    pyxel.text(start_x + 8, start_y + 8, str(instance.pen_size), 7)
    pyxel.blt(start_x + 14, start_y + 8, 0, 0, 0, 5, 5)

    pyxel.text(start_x, start_y + 18, "PARTICLE", 7)
    pyxel.blt(start_x, start_y + 26, 0, 16, 5, 15, 5)
    pyxel.blt(start_x + 18, start_y + 26, 0, 0, 10, 15, 5)
