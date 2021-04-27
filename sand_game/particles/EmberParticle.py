from __future__ import annotations
from random import randint
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sand_game.canvas import CanvasController
from sand_game.particles.Particle import Particle


class EmberParticle(Particle):
    def __init__(self, max_tick: int) -> None:
        """Creates the ember

        Args:
            max_tick (int): The amount of time to burn for before disappearing
        """
        super().__init__(color=14)
        self.tick = 0
        self.max_tick = max_tick

    def update(self, x: int, y: int, canvas: CanvasController) -> None:
        from sand_game.particles.FireParticle import FireParticle
        from sand_game.particles.WaterParticle import WaterParticle

        self.updated = True
        self.fall(x, y, canvas)

        # Random chance to spread based on the burnability of the current object
        if randint(0, self.max_tick) == 1:
            for loc in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                particle = canvas.get(loc[0], loc[1])
                if particle is None:
                    canvas.set(loc[0], loc[1], FireParticle())
                    continue

                if isinstance(particle, WaterParticle):
                    canvas.set(x, y, None)

                if particle.burntime >= 0:
                    canvas.set(loc[0], loc[1], EmberParticle(particle.burntime))

        if self.tick == self.max_tick:
            canvas.set(x, y, None)
            return

        self.tick = self.tick + 1
