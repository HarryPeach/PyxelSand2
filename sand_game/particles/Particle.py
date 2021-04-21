from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sand_game.canvas import CanvasController

import random


class Particle:

    def __init__(self):
        self.updated = False
        self.color = 0

    def update(self, x: int, y: int, canvas: CanvasController):
        """Called when the particle must update its state
        """
        pass

    def fall(self, x: int, y: int, canvas: CanvasController):
        if y == canvas.height - 1:
            return

        if canvas.get(x, y + 1) is None:  # If there is no particle below
            canvas.set(x, y + 1, canvas.get(x, y))
            canvas.set(x, y, None)
            return

        dx_choice = random.choice([-1, 1])

        # If there is no particle to the sides of the particle
        if canvas.get(x + dx_choice, y + 1) is None:
            canvas.set(x + dx_choice, y + 1, canvas.get(x, y))
            canvas.set(x, y, None)
