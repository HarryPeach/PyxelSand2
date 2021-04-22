from sand_game.__main__ import SandGame
from sand_game.particles.SandParticle import SandParticle
from unittest.mock import patch
from typing import Callable, Any

from expects import expect, equal, be


class TestSandGame():
    """Tests the core game class
    """

    @patch("pyxel.run")
    def test_simulation_pause(_, mock_req: Callable[[], Any]) -> None:
        """Tests that a canvas is successfully created
        """
        mock_req.side_effect = None
        game = SandGame()
        game.canvas_controller.set(0, 0, SandParticle())
        game.update()
