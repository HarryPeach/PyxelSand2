from __future__ import annotations
from sand_game.particles.EmberParticle import EmberParticle
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sand_game.canvas import CanvasController
from sand_game.particles.Particle import Particle
from sand_game.particles.WaterParticle import WaterParticle
from random import randint


class FireParticle(Particle):

    def __init__(self) -> None:
        self.updated = False
        self.color = 8
        self.tick = 0
        self.burntime = -1
        self.max_tick = randint(0, 30)

    def update(self, x: int, y: int, canvas: CanvasController) -> None:
        if self.tick == self.max_tick:
            canvas.set(x, y, None)
            return

        self.tick = self.tick + 1
        self.fall(x, y, canvas, direction=-1, fill_space=True)

        for loc in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            particle = canvas.get(loc[0], loc[1])
            if particle is None:
                continue

            if isinstance(particle, WaterParticle):
                canvas.set(x, y, None)

            if particle.burntime >= 0:
                canvas.set(loc[0], loc[1], EmberParticle(particle.burntime))
