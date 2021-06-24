from sand_game.particles.Particle import Particle
from sand_game.particles.SandParticle import SandParticle


class GameState():
    """Keeps the current global game state
    """

    # The current particle that is selected
    current_particle: Particle = SandParticle

    # Whether the game is paused or not
    paused: bool = False

    # The size of the pen
    pen_size: int = 2

    @classmethod
    def set_current_particle(cls, particle: Particle):
        cls.current_particle = particle

    @classmethod
    def set_paused(cls, pause: bool):
        cls.paused = pause

    @classmethod
    def set_pen_size(cls, size: int):
        if size < 1 or size > 9:
            return
        cls.pen_size = size
