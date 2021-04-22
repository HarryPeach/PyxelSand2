from sand_game.canvas import CanvasController
from sand_game.__main__ import SandGame
from sand_game.particles.SandParticle import SandParticle
from expects import expect, be, be_none

import sys


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
        sys.modules["pyxel"] = None
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
