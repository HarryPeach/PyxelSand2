# Stop pyxel from being imported during a test as this can cause test failures due to
# the CI test environment not supporting graphics
import sys
from unittest.mock import MagicMock
sys.modules["pyxel"] = MagicMock()

from sand_game.canvas import CanvasController  # noqa
from sand_game.__main__ import SandGame  # noqa
from sand_game.particles.SandParticle import SandParticle  # noqa
from expects import expect, be, be_none  # noqa


class SandGameWithoutInit(SandGame):
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
        game = SandGameWithoutInit()
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
