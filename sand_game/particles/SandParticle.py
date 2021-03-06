from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sand_game.canvas import CanvasController
from sand_game.particles.Particle import Particle


class SandParticle(Particle):
    uuid = "sand"

    def __init__(self) -> None:
        super().__init__(color=15, burntime=10)

    def update(self, x: int, y: int, canvas: CanvasController) -> None:
        self.updated = True
        self.fall(x, y, canvas)
