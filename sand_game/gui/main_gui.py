from sand_game.game_state import GameState
from sand_game.particles.WaterParticle import WaterParticle
from sand_game.particles.FuseParticle import FuseParticle
from sand_game.particles.AcidParticle import AcidParticle
from sand_game.particles.FireParticle import FireParticle
from sand_game.particles.WallParticle import WallParticle
from sand_game.particles.SandParticle import SandParticle
# from typing import TYPE_CHECKING
# if TYPE_CHECKING:
# from sand_game.__main__ import SandGame
from sand_game.gui.gui import Gui, Label, TexturedButton


class MainGui(Gui):
    """Represents the main game GUI including available particles, all buttons, and
    all text
    """

    def __init__(self, start_x: int, start_y: int, game) -> None:
        super(MainGui, self).__init__(start_x, start_y)
        self.game = game

        self._gui_pause_button = TexturedButton(lambda: GameState.set_paused(True), 0,
                                                0, 10, 0, 5, 5, tooltip="Pause")
        self.add_button(self._gui_pause_button)
        self._gui_play_button = TexturedButton(lambda: GameState.set_paused(False), 0,
                                               0, 15, 0, 5, 5, hidden=True,
                                               tooltip="Resume")
        self.add_button(self._gui_play_button)

        self.add_button(TexturedButton(lambda: self.game.canvas_controller.clear(), 6,
                                       0, 20, 0, 5, 5, tooltip="Clear"))

        self._gui_overwrite_button_enable = TexturedButton(
            lambda: GameState.set_overwrite(True), 12, 0, 30, 0, 5, 5,
            tooltip="Overwrite"
        )
        self.add_button(self._gui_overwrite_button_enable)

        self._gui_overwrite_button_disable = TexturedButton(
            lambda: GameState.set_overwrite(False), 12, 0, 25, 0, 5, 5, hidden=True,
            tooltip="Overwrite"
        )
        self.add_button(self._gui_overwrite_button_disable)

        self._gui_import_button = TexturedButton(
            self.game.import_canvas, 18, 0, 35, 0, 5, 5,
            tooltip="Import"
        )
        self.add_button(self._gui_import_button)

        self._gui_import_button = TexturedButton(
            self.game.export_canvas, 24, 0, 40, 0, 5, 5,
            tooltip="Export"
        )
        self.add_button(self._gui_import_button)

        # Pen size gui items
        self.add_label(Label("Pen Size:", 0, 10, 7))
        self._gui_pen_label = Label(str(GameState.pen_size), 11, 18, 7)
        self.add_button(
            TexturedButton(lambda: GameState.set_pen_size(GameState.pen_size - 1),
                           0, 18, 5, 0, 5, 5, tooltip="Pen --"))
        self.add_label(self._gui_pen_label)
        self.add_button(
            TexturedButton(lambda: GameState.set_pen_size(GameState.pen_size + 1),
                           20, 18, 0, 0, 5, 5, tooltip="Pen ++"))

        # Particle gui items
        self.add_label(Label("Particles: ", 0, 26, 7))
        self._gui_sand_button = TexturedButton(
            lambda: GameState.set_current_particle(SandParticle),
            0, 34, 0, 5, 15, 5, tooltip="Sand")
        self.add_button(self._gui_sand_button)
        self._gui_wall_button = TexturedButton(
            lambda: GameState.set_current_particle(WallParticle),
            16, 34, 0, 10, 15, 5, tooltip="Wall"
        )
        self.add_button(self._gui_wall_button)
        self._gui_water_button = TexturedButton(
            lambda: GameState.set_current_particle(WaterParticle),
            0, 40, 0, 15, 15, 5, tooltip="Water"
        )
        self.add_button(self._gui_water_button)

        self._gui_fire_button = TexturedButton(
            lambda: GameState.set_current_particle(FireParticle),
            16, 40, 0, 20, 15, 5, tooltip="Fire"
        )
        self.add_button(self._gui_fire_button)

        self._gui_acid_button = TexturedButton(
            lambda: GameState.set_current_particle(AcidParticle),
            0, 46, 0, 25, 15, 5, tooltip="Acid"
        )
        self.add_button(self._gui_acid_button)

        self._gui_fuse_button = TexturedButton(
            lambda: GameState.set_current_particle(FuseParticle),
            16, 46, 0, 30, 15, 5, tooltip="Fuse"
        )
        self.add_button(self._gui_fuse_button)

    def update_gui_items(self) -> None:
        """Updates all of the items within the GUI
        """
        self._gui_pen_label.set_value(str(GameState.pen_size))

        self._gui_sand_button.set_enabled(
            GameState.current_particle == SandParticle
        )
        self._gui_wall_button.set_enabled(
            GameState.current_particle == WallParticle
        )
        self._gui_water_button.set_enabled(
            GameState.current_particle == WaterParticle
        )
        self._gui_fire_button.set_enabled(
            GameState.current_particle == FireParticle
        )
        self._gui_acid_button.set_enabled(
            GameState.current_particle == AcidParticle
        )
        self._gui_fuse_button.set_enabled(
            GameState.current_particle == FuseParticle
        )

        self._gui_pause_button.set_hidden(GameState.paused)
        self._gui_play_button.set_hidden(not GameState.paused)

        self._gui_overwrite_button_enable.set_hidden(GameState.overwrite)
        self._gui_overwrite_button_disable.set_hidden(not GameState.overwrite)
