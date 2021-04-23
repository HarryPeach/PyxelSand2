from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sand_game.canvas import CanvasController
from sand_game.particles.Particle import Particle


class FireParticle(Particle):

    def __init__(self) -> None:
        self.updated = False
        self.color = 8
        self.tick = 0

    def update(self, x: int, y: int, canvas: CanvasController) -> None:
        if self.tick == 5:
            canvas.set(x, y, None)

        self.tick = self.tick + 1
