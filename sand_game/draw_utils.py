import pyxel


def draw_cursor(width: int, color: int, canvas_width: int, canvas_height: int,
                canvas_start_loc: tuple[int, int]) -> None:
    """Draws the cursor

    Args:
        width (int): The width of the cursor
        color (int): The color to draw
        canvas_width (int): The width of the canvas
        canvas_height (int): The height of the canvas
        canvas_start_loc (tuple[int, int]): The starting location of the canvas
    """
    pyxel.circb(pyxel.mouse_x, pyxel.mouse_y, width, color)
