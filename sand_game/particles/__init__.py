from sand_game.particles.WallParticle import WallParticle
from sand_game.particles.SandParticle import SandParticle
from sand_game.particles.FireParticle import FireParticle
from sand_game.particles.EmberParticle import EmberParticle
from sand_game.particles.AcidParticle import AcidParticle
from sand_game.particles.WaterParticle import WaterParticle

uuid_map = {
    "sand": SandParticle,
    "wall": WallParticle,
    "water": WaterParticle,
    "acid": AcidParticle,
    "ember": EmberParticle,
    "fire": FireParticle
}
