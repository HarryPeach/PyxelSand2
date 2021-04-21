from sand_game.particles.Particle import Particle
from sand_game.canvas import CanvasController


class SandParticle(Particle):
    def __init__(self):
        self.updated = False
        self.color = 12

    def update(self, x: int, y: int, canvas: CanvasController):
        """Called when the particle must update its state

        Args:
            x (int): The current x location of the particle
            y (int): The current y location of the particle
            canvas (CanvasController): The current canvas' controller
        """
        self.updated = True
        self.fall(x, y, canvas)
