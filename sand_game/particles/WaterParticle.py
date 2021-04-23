from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sand_game.canvas import CanvasController
from sand_game.particles.Particle import Particle


class WaterParticle(Particle):
    def __init__(self):
        self.updated = False
        self.color = 5

    def update(self, x: int, y: int, canvas: CanvasController):
        self.updated = True
        # self.fall(x, y, canvas)
