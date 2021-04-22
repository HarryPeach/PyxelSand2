# Stop pyxel from being imported during a test as this can cause test failures due to
# the CI test environment not supporting graphics
from sand_game.particles.WallParticle import WallParticle
import sys
from unittest.mock import MagicMock
sys.modules["pyxel"] = MagicMock()

from sand_game.canvas import CanvasController  # noqa
from sand_game.__main__ import SandGame  # noqa
from sand_game.particles.SandParticle import SandParticle  # noqa
from expects import expect, be, be_none, be_a  # noqa


class SandGameTestImpl(SandGame):
    """A child of the SandGame class that re-implements certain methods for
    ease-of-testing
    """
    def __init__(self):
        self.canvas_controller = CanvasController(100, 100)
        self.canvas_width = 100
        self.canvas_height = 100
        self.paused = False


class TestSandGame():
    """Tests the core game class
    """

    def test_simulation_pause(_) -> None:
        """Tests that when a simulation is paused, a particle does not update
        """
        game = SandGameTestImpl()
        sp = SandParticle()
        game.canvas_controller.set(0, 0, sp)

        game._set_paused(True)
        game._update_particles()

        expect(game.canvas_controller.get(0, 1)).to(be_none)
        expect(game.canvas_controller.get(0, 0)).to(be(sp))

        game._set_paused(False)
        game._update_particles()

        expect(game.canvas_controller.get(0, 0)).to(be_none)
        expect(game.canvas_controller.get(0, 1)).to(be(sp))

    def test_overwrite(_) -> None:
        """Tests that the game correctly enforces the overwrite check
        """
        game = SandGameTestImpl()
        game.canvas_controller.set(10, 10, SandParticle())

        game.overwrite = False
        game._place_particle(WallParticle, 10, 10, 4)

        expect(game.canvas_controller.get(10, 10)).to(be_a(SandParticle))
        expect(game.canvas_controller.get(10, 9)).to(be_a(WallParticle))
        expect(game.canvas_controller.get(10, 11)).to(be_a(WallParticle))
        expect(game.canvas_controller.get(9, 10)).to(be_a(WallParticle))
        expect(game.canvas_controller.get(11, 10)).to(be_a(WallParticle))

        game.overwrite = True
        game._place_particle(WallParticle, 10, 10, 4)
        expect(game.canvas_controller.get(10, 10)).to(be_a(WallParticle))
