import pyxel


def draw_cursor(width: int, color: int) -> None:
    """Draws the cursor

    Args:
        width (int): The width of the cursor
        color (int): The color to draw
    """
    pyxel.circb(pyxel.mouse_x, pyxel.mouse_y, width, color)
