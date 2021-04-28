from sand_game.particles.AcidParticle import AcidParticle
from sand_game.particles.FireParticle import FireParticle
from sand_game.particles.WaterParticle import WaterParticle
from sand_game.particles.SandParticle import SandParticle
from sand_game.particles.WallParticle import WallParticle
from sand_game.particles.Particle import Particle
from sand_game.canvas import CanvasController
from sand_game.draw_utils import draw_cursor
from sand_game.gui import Gui, TexturedButton, Label
from typing import Union
from itertools import product
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename, askopenfilename
from sand_game import __version__
import pyxel
import os


class SandGame:
    def __init__(self) -> None:
        pyxel.init(160, 120, fps=60, caption=f"Sand Game v{__version__}")

        pyxel.load("assets/res.pyxres")

        self.canvas_width = 100
        self.canvas_height = 100
        self.canvas_start_loc = (8, 14)

        self.canvas_controller = CanvasController(
            self.canvas_width, self.canvas_height)

        self.pen_size = 2
        self.paused = False
        self.current_particle = SandParticle
        self.overwrite = False

        self.gui = Gui(114, 14)

        self._gui_pause_button = TexturedButton(lambda: self._set_paused(True), 0, 0,
                                                10, 0, 5, 5, tooltip="Pause")
        self.gui.add_button(self._gui_pause_button)
        self._gui_play_button = TexturedButton(lambda: self._set_paused(False), 0, 0,
                                               15, 0, 5, 5, hidden=True,
                                               tooltip="Resume")
        self.gui.add_button(self._gui_play_button)

        self.gui.add_button(TexturedButton(lambda: self.canvas_controller.clear(), 6,
                                           0, 20, 0, 5, 5, tooltip="Clear"))

        self._gui_overwrite_button_enable = TexturedButton(
            lambda: self._set_overwrite(True), 12, 0, 30, 0, 5, 5,
            tooltip="Overwrite"
        )
        self.gui.add_button(self._gui_overwrite_button_enable)

        self._gui_overwrite_button_disable = TexturedButton(
            lambda: self._set_overwrite(False), 12, 0, 25, 0, 5, 5, hidden=True,
            tooltip="Overwrite"
        )
        self.gui.add_button(self._gui_overwrite_button_disable)

        self._gui_import_button = TexturedButton(
            self.import_canvas, 18, 0, 35, 0, 5, 5,
            tooltip="Import"
        )
        self.gui.add_button(self._gui_import_button)

        self._gui_import_button = TexturedButton(
            self.export_canvas, 24, 0, 40, 0, 5, 5,
            tooltip="Export"
        )
        self.gui.add_button(self._gui_import_button)

        # Pen size gui items
        self.gui.add_label(Label("Pen Size:", 0, 10, 7))
        self._gui_pen_label = Label(str(self.pen_size), 11, 18, 7)
        self.gui.add_button(
            TexturedButton(lambda: self._set_pen_size(self.pen_size - 1),
                           0, 18, 5, 0, 5, 5, tooltip="Pen --"))
        self.gui.add_label(self._gui_pen_label)
        self.gui.add_button(
            TexturedButton(lambda: self._set_pen_size(self.pen_size + 1),
                           20, 18, 0, 0, 5, 5, tooltip="Pen ++"))

        # Particle gui items
        self.gui.add_label(Label("Particles: ", 0, 26, 7))
        self._gui_sand_button = TexturedButton(
            lambda: self._set_current_particle(SandParticle),
            0, 34, 0, 5, 15, 5, tooltip="Sand")
        self.gui.add_button(self._gui_sand_button)
        self._gui_wall_button = TexturedButton(
            lambda: self._set_current_particle(WallParticle),
            16, 34, 0, 10, 15, 5, tooltip="Wall"
        )
        self.gui.add_button(self._gui_wall_button)
        self._gui_water_button = TexturedButton(
            lambda: self._set_current_particle(WaterParticle),
            0, 40, 0, 15, 15, 5, tooltip="Water"
        )
        self.gui.add_button(self._gui_water_button)

        self._gui_fire_button = TexturedButton(
            lambda: self._set_current_particle(FireParticle),
            16, 40, 0, 20, 15, 5, tooltip="Fire"
        )
        self.gui.add_button(self._gui_fire_button)

        self._gui_acid_button = TexturedButton(
            lambda: self._set_current_particle(AcidParticle),
            0, 46, 0, 25, 15, 5, tooltip="Acid"
        )
        self.gui.add_button(self._gui_acid_button)

        pyxel.run(self.update, self.draw)

    def _set_current_particle(self, particle: Particle) -> None:
        self.current_particle = particle

    def _set_pen_size(self, new_size: int) -> None:
        if new_size < 1 or new_size > 9:
            return
        self.pen_size = new_size

    def _set_paused(self, paused: bool) -> None:
        self.paused = paused

    def _set_overwrite(self, overwrite: bool) -> None:
        self.overwrite = overwrite

    def export_canvas(self) -> None:
        """Saves the current canvas to a file
        """
        filename = self.open_filepicker(True)
        if filename != "":
            if os.path.splitext(filename)[1] == ".cnv":
                self.canvas_controller.save_to_file(filename, True)
            else:
                self.canvas_controller.save_to_file(filename, False)

    def import_canvas(self) -> None:
        """Loads the current canvas from a file
        """
        filename = self.open_filepicker(False)
        if filename != "":
            self.paused = True
            self.canvas_controller = CanvasController.load_from_file(filename)

    def open_filepicker(self, new: bool = False) -> str:
        """Opens a GUI filepicker

        Args:
            new (bool, optional): Whether the file needs to be created.
            Defaults to False.

        Returns:
            str: The filename picked by the user, "" if cancelled.
        """
        result = None

        if new:
            result = asksaveasfilename(initialfile="export",
                                       filetypes=[("Compressed Canvas", ".cnv"),
                                                  ("JSON Canvas", ".json")],
                                       defaultextension=".json",
                                       title="Export canvas")
        else:
            result = askopenfilename(initialfile="import", title="Import canvas")

        return result

    def place_particle(self, particle: Union[Particle, None], center_x: int,
                       center_y: int, radius: int) -> None:
        """Places particles at the given location in a circle

        Args:
            particle (Union[Particle, None]): The particle to place, or None to
            clear the location
            center_x (int): The x-coordinate for the center of the circle
            center_y (int): The y-coordinate for the center of the circle
            radius (int): The radius of the circle
        """
        for y, x in product(range(-radius, radius), repeat=2):
            if (x * x + y * y > radius * radius):
                continue

            if particle is None:
                self.canvas_controller.set(
                    center_x + x, center_y + y, None)
            else:
                # Check if overwrite is enabled before placing
                if self._can_place_particle(center_x + x, center_y + y):
                    self.canvas_controller.set(center_x + x, center_y + y,
                                               particle())

    def _can_place_particle(self, x: int, y: int) -> bool:
        """Whether a particle is allowed to be placed at the current location based
        on current overwrite rules

        Args:
            x (int): The x co-ordinate of the particle
            y (int): The y co-ordinate of the particle

        Returns:
            bool: Whether the particle can be placed
        """
        particle_at = self.canvas_controller.get(x, y)
        if not self.overwrite and particle_at is not None:
            return False
        else:
            return True

    def update(self) -> None:
        """Updates all of the items in the game
        """
        if pyxel.btnp(pyxel.KEY_SPACE):
            self._set_paused(not self.paused)

        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.gui.handle_click(pyxel.mouse_x, pyxel.mouse_y)

        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
            self.place_particle(self.current_particle, pyxel.mouse_x -
                                self.canvas_start_loc[0],
                                pyxel.mouse_y - self.canvas_start_loc[1],
                                self.pen_size)

        if pyxel.btn(pyxel.MOUSE_RIGHT_BUTTON):
            self.place_particle(
                None, pyxel.mouse_x - self.canvas_start_loc[0],
                pyxel.mouse_y - self.canvas_start_loc[1], self.pen_size)

        if pyxel.mouse_wheel == 1:
            self._set_pen_size(self.pen_size + 1)
        if pyxel.mouse_wheel == -1:
            self._set_pen_size(self.pen_size - 1)

        self._update_gui_items()
        self._update_particles()

    def _update_gui_items(self) -> None:
        self._gui_pen_label.set_value(str(self.pen_size))

        self._gui_sand_button.set_enabled(
            self.current_particle == SandParticle
        )
        self._gui_wall_button.set_enabled(
            self.current_particle == WallParticle
        )
        self._gui_water_button.set_enabled(
            self.current_particle == WaterParticle
        )
        self._gui_fire_button.set_enabled(
            self.current_particle == FireParticle
        )
        self._gui_acid_button.set_enabled(
            self.current_particle == AcidParticle
        )

        self._gui_pause_button.set_hidden(self.paused)
        self._gui_play_button.set_hidden(not self.paused)

        self._gui_overwrite_button_enable.set_hidden(self.overwrite)
        self._gui_overwrite_button_disable.set_hidden(not self.overwrite)

    def _update_particles(self) -> None:
        if self.paused:
            return

        # Update every particle
        for x in range(self.canvas_width):
            for y in range(self.canvas_height):
                particle = self.canvas_controller.get(x, y)
                if particle is None:
                    continue

                if particle.updated:
                    continue

                particle.update(x, y, self.canvas_controller)

        # Reset the updated status of every particle to false
        for particle in self.canvas_controller.data:
            if particle is None:
                continue
            particle.updated = False

    def draw(self) -> None:
        """Draws all items in the game
        """
        pyxel.cls(1)

        pyxel.text(8, 5, f"Sand Game v{__version__}", 7)
        pyxel.rect(self.canvas_start_loc[0] - 1, self.canvas_start_loc[1] - 1,
                   self.canvas_width + 2, self.canvas_height + 2, 8)
        pyxel.rect(self.canvas_start_loc[0], self.canvas_start_loc[1],
                   self.canvas_width, self.canvas_height, 0)

        # Draw every particle
        for x in range(self.canvas_width):
            for y in range(self.canvas_height):
                particle = self.canvas_controller.get(x, y)
                if particle is not None:
                    pyxel.pset(
                        x + self.canvas_start_loc[0], y + self.canvas_start_loc[1],
                        particle.color
                    )

        self.gui.draw()
        self.gui.handle_hover(pyxel.mouse_x, pyxel.mouse_y)
        draw_cursor(self.pen_size - 1, 7)


if __name__ == "__main__":
    Tk().withdraw()
    SandGame()
