from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sand_game.canvas import CanvasController
from sand_game.particles.Particle import Particle


class WaterParticle(Particle):
    def __init__(self) -> None:
        super().__init__(color=5)

    def update(self, x: int, y: int, canvas: CanvasController) -> None:
        self.updated = True
        self.fill_space(x, y, canvas)
        # self.fall(x, y, canvas)
