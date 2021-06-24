from sand_game.main_gui import MainGui
from sand_game.particles.SandParticle import SandParticle
from sand_game.game_state import GameState
from sand_game.particles.Particle import Particle
from sand_game.canvas import CanvasController
from sand_game.draw_utils import draw_cursor
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

        self.gui = MainGui(114, 14, self)

        pyxel.run(self.update, self.draw)

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
            GameState.paused = True
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
            result = askopenfilename(
                initialfile="import", title="Import canvas")

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
        if not GameState.overwrite and particle_at is not None:
            return False
        else:
            return True

    def update(self) -> None:
        """Updates all of the items in the game
        """
        if pyxel.btnp(pyxel.KEY_SPACE):
            GameState.set_paused(not GameState.paused)

        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.gui.handle_click(pyxel.mouse_x, pyxel.mouse_y)

        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
            self.place_particle(GameState.current_particle, pyxel.mouse_x -
                                self.canvas_start_loc[0],
                                pyxel.mouse_y - self.canvas_start_loc[1],
                                GameState.pen_size)

        if pyxel.btn(pyxel.MOUSE_RIGHT_BUTTON):
            self.place_particle(
                None, pyxel.mouse_x - self.canvas_start_loc[0],
                pyxel.mouse_y - self.canvas_start_loc[1], GameState.pen_size)

        if pyxel.mouse_wheel == 1:
            GameState.set_pen_size(GameState.pen_size + 1)
        if pyxel.mouse_wheel == -1:
            GameState.set_pen_size(GameState.pen_size - 1)

        self.gui.update_gui_items()
        self._update_particles()

    def _update_particles(self) -> None:
        if GameState.paused:
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
                        x + self.canvas_start_loc[0], y +
                        self.canvas_start_loc[1],
                        particle.color
                    )

        self.gui.draw()
        self.gui.handle_hover(pyxel.mouse_x, pyxel.mouse_y)
        draw_cursor(GameState.pen_size - 1, 7, self.canvas_width,
                    self.canvas_height, self.canvas_start_loc)


if __name__ == "__main__":
    Tk().withdraw()
    SandGame()
