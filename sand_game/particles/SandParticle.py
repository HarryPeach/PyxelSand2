from sand_game.particles.Particle import Particle
from sand_game.canvas import CanvasController


class SandParticle(Particle):
    def __init__(self):
        self.updated = False
        self.color = 12

    def update(self, x: int, y: int, canvas: CanvasController):
        self.updated = True
        self.fall(x, y, canvas)
