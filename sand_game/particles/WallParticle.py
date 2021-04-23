from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sand_game.canvas import CanvasController
from sand_game.particles.Particle import Particle


class WallParticle(Particle):
    def __init__(self) -> None:
        self.updated = False
        self.color = 13

    def update(self, x: int, y: int, canvas: CanvasController) -> None:
        """Called when the particle must update its state

        Args:
            x (int): The current x location of the particle
            y (int): The current y location of the particle
            canvas (CanvasController): The current canvas' controller
        """
        self.updated = True
