from __future__ import annotations
from sand_game.particles.EmberParticle import EmberParticle
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sand_game.canvas import CanvasController
from sand_game.particles.Particle import Particle
from sand_game.particles.WaterParticle import WaterParticle
from random import randint


class AcidParticle(Particle):

    def __init__(self) -> None:
        super().__init__(color=11)
        self.tick = 0
        self.max_tick = randint(0, 30)

    def update(self, x: int, y: int, canvas: CanvasController) -> None:
        self.fall(x, y, canvas, direction=-1, fill_space=True)

        if (self.tick == self.max_tick):
            # Check particles around for flammability
            for loc in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                particle = canvas.get(loc[0], loc[1])
                if particle is None:
                    continue

                canvas.set(loc[0], loc[1], AcidParticle())

        self.tick = self.tick + 1
