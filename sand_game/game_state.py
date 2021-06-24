from sand_game.particles.Particle import Particle
from sand_game.particles.SandParticle import SandParticle


class GameState():
    """Keeps the current global game state
    """

    # The current particle that is selected
    current_particle: Particle = SandParticle

    # Whether the game is paused or not
    paused: bool = False

    @classmethod
    def set_current_particle(cls, particle: Particle):
        cls.current_particle = particle

    @classmethod
    def set_paused(cls, pause: bool):
        cls.paused = pause
