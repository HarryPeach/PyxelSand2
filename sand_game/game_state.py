from sand_game.particles.Particle import Particle
from sand_game.particles.SandParticle import SandParticle


class GameState():

    current_particle: Particle = SandParticle

    @classmethod
    def set_current_particle(cls, particle: Particle):
        cls.current_particle = particle
