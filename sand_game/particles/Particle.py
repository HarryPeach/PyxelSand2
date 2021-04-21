from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sand_game.canvas import CanvasController


class Particle:

    def __init__(self):
        self.updated = False
        self.color = 0

    def update(self, canvas: CanvasController):
        """Called when the particle must update its state
        """
