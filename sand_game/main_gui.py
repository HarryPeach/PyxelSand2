from sand_game.particles.WaterParticle import WaterParticle
from sand_game.particles.FuseParticle import FuseParticle
from sand_game.particles.AcidParticle import AcidParticle
from sand_game.particles.FireParticle import FireParticle
from sand_game.particles.WallParticle import WallParticle
from sand_game.particles.SandParticle import SandParticle
# from typing import TYPE_CHECKING
# if TYPE_CHECKING:
# from sand_game.__main__ import SandGame
from sand_game.gui import Gui, Label, TexturedButton


class MainGui():
    """A wrapper class around Gui, to represent the main game Gui
    """

    def __init__(self, start_x: int, start_y: int, game) -> None:
        # self.gui = super(MainGui, self).__init__(start_x, start_y)
        self.gui = Gui(start_x, start_y)
        self.start_x = start_x
        self.start_y = start_y
        self.game = game

        self._gui_pause_button = TexturedButton(lambda: self.game._set_paused(True), 0, 0,
                                                10, 0, 5, 5, tooltip="Pause")
        self.gui.add_button(self._gui_pause_button)
        self._gui_play_button = TexturedButton(lambda: self.game._set_paused(False), 0, 0,
                                               15, 0, 5, 5, hidden=True,
                                               tooltip="Resume")
        self.gui.add_button(self._gui_play_button)

        self.gui.add_button(TexturedButton(lambda: self.game.canvas_controller.clear(), 6,
                                           0, 20, 0, 5, 5, tooltip="Clear"))

        self._gui_overwrite_button_enable = TexturedButton(
            lambda: self.game._set_overwrite(True), 12, 0, 30, 0, 5, 5,
            tooltip="Overwrite"
        )
        self.gui.add_button(self._gui_overwrite_button_enable)

        self._gui_overwrite_button_disable = TexturedButton(
            lambda: self.game._set_overwrite(False), 12, 0, 25, 0, 5, 5, hidden=True,
            tooltip="Overwrite"
        )
        self.gui.add_button(self._gui_overwrite_button_disable)

        self._gui_import_button = TexturedButton(
            self.game.import_canvas, 18, 0, 35, 0, 5, 5,
            tooltip="Import"
        )
        self.gui.add_button(self._gui_import_button)

        self._gui_import_button = TexturedButton(
            self.game.export_canvas, 24, 0, 40, 0, 5, 5,
            tooltip="Export"
        )
        self.gui.add_button(self._gui_import_button)

        # Pen size gui items
        self.gui.add_label(Label("Pen Size:", 0, 10, 7))
        self._gui_pen_label = Label(str(self.game.pen_size), 11, 18, 7)
        self.gui.add_button(
            TexturedButton(lambda: self.game._set_pen_size(self.game.pen_size - 1),
                           0, 18, 5, 0, 5, 5, tooltip="Pen --"))
        self.gui.add_label(self._gui_pen_label)
        self.gui.add_button(
            TexturedButton(lambda: self.game._set_pen_size(self.game.pen_size + 1),
                           20, 18, 0, 0, 5, 5, tooltip="Pen ++"))

        # Particle gui items
        self.gui.add_label(Label("Particles: ", 0, 26, 7))
        self._gui_sand_button = TexturedButton(
            lambda: self.game._set_current_particle(SandParticle),
            0, 34, 0, 5, 15, 5, tooltip="Sand")
        self.gui.add_button(self._gui_sand_button)
        self._gui_wall_button = TexturedButton(
            lambda: self.game._set_current_particle(WallParticle),
            16, 34, 0, 10, 15, 5, tooltip="Wall"
        )
        self.gui.add_button(self._gui_wall_button)
        self._gui_water_button = TexturedButton(
            lambda: self.game._set_current_particle(WaterParticle),
            0, 40, 0, 15, 15, 5, tooltip="Water"
        )
        self.gui.add_button(self._gui_water_button)

        self._gui_fire_button = TexturedButton(
            lambda: self.game._set_current_particle(FireParticle),
            16, 40, 0, 20, 15, 5, tooltip="Fire"
        )
        self.gui.add_button(self._gui_fire_button)

        self._gui_acid_button = TexturedButton(
            lambda: self.game._set_current_particle(AcidParticle),
            0, 46, 0, 25, 15, 5, tooltip="Acid"
        )
        self.gui.add_button(self._gui_acid_button)

        self._gui_fuse_button = TexturedButton(
            lambda: self.game._set_current_particle(FuseParticle),
            16, 46, 0, 30, 15, 5, tooltip="Fuse"
        )
        self.gui.add_button(self._gui_fuse_button)

    def draw(self):
        self.gui.draw()

    def handle_hover(self, mouse_x: int, mouse_y: int):
        self.gui.handle_hover(mouse_x, mouse_y)

    def handle_click(self, mouse_x: int, mouse_y: int):
        self.gui.handle_click(mouse_x, mouse_y)

    def update_gui_items(self) -> None:
        self._gui_pen_label.set_value(str(self.game.pen_size))

        self._gui_sand_button.set_enabled(
            self.game.current_particle == SandParticle
        )
        self._gui_wall_button.set_enabled(
            self.game.current_particle == WallParticle
        )
        self._gui_water_button.set_enabled(
            self.game.current_particle == WaterParticle
        )
        self._gui_fire_button.set_enabled(
            self.game.current_particle == FireParticle
        )
        self._gui_acid_button.set_enabled(
            self.game.current_particle == AcidParticle
        )
        self._gui_fuse_button.set_enabled(
            self.game.current_particle == FuseParticle
        )

        self._gui_pause_button.set_hidden(self.game.paused)
        self._gui_play_button.set_hidden(not self.game.paused)

        self._gui_overwrite_button_enable.set_hidden(self.game.overwrite)
        self._gui_overwrite_button_disable.set_hidden(not self.game.overwrite)
