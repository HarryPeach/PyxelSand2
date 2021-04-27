from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sand_game.canvas import CanvasController
from sand_game.particles.Particle import Particle
from random import randint


class AcidParticle(Particle):

    def __init__(self) -> None:
        super().__init__(color=11)
        self.tick = 0
        self.max_tick = randint(0, 100)

    def update(self, x: int, y: int, canvas: CanvasController) -> None:
        self.updated = True
        self.fall(x, y, canvas, fill_space=True)

        if (self.tick == self.max_tick):
            if randint(0, 5) == 1:
                canvas.set(x, y, None)
                return

            # Check particles around for flammability
            for loc in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                particle = canvas.get(loc[0], loc[1])
                if particle is None:
                    continue

                canvas.set(loc[0], loc[1], AcidParticle())
            self.tick = 0

        self.tick = self.tick + 1
