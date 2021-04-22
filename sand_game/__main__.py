from sand_game.particles.SandParticle import SandParticle
from sand_game.particles.WallParticle import WallParticle
from sand_game.particles.Particle import Particle
from sand_game.canvas import CanvasController
from sand_game.draw_utils import draw_cursor
from sand_game.gui import Gui, TexturedButton, Label
from typing import Union
import pyxel


class SandGame:
    def __init__(self):
        pyxel.init(160, 120, fps=60, caption="Sand Game")

        pyxel.load("assets/res.pyxres")

        self.canvas_width = 100
        self.canvas_height = 100
        self.canvas_start_loc = (10, 10)

        self.canvas_controller = CanvasController(
            self.canvas_width, self.canvas_height)

        self.pen_size = 2
        self.paused = False
        self.current_particle = SandParticle
        self.overwrite = False

        self.gui = Gui(114, 10)

        self._gui_pause_button = TexturedButton(lambda: self._set_paused(True), 0, 0,
                                                10, 0, 5, 5)
        self.gui.add_button(self._gui_pause_button)
        self._gui_play_button = TexturedButton(lambda: self._set_paused(False), 0, 0,
                                               15, 0, 5, 5)
        self.gui.add_button(self._gui_play_button)

        self.gui.add_button(TexturedButton(lambda: self.canvas_controller.clear(), 6,
                                           0, 20, 0, 5, 5))

        # Pen size gui items
        self.gui.add_text(Label("Pen Size:", 0, 10, 7))
        self._gui_pen_label = Label(str(self.pen_size), 11, 18, 7)
        self.gui.add_button(
            TexturedButton(lambda: self._set_pen_size(self.pen_size - 1),
                           0, 18, 5, 0, 5, 5))
        self.gui.add_text(self._gui_pen_label)
        self.gui.add_button(
            TexturedButton(lambda: self._set_pen_size(self.pen_size + 1),
                           20, 18, 0, 0, 5, 5))

        # Particle gui items
        self.gui.add_text(Label("Particles: ", 0, 26, 7))
        self._gui_sand_button = TexturedButton(
            lambda: self._set_current_particle(SandParticle),
            0, 34, 0, 5, 15, 5)
        self.gui.add_button(self._gui_sand_button)
        self._gui_wall_button = TexturedButton(
            lambda: self._set_current_particle(WallParticle),
            16, 34, 0, 10, 15, 5
        )
        self.gui.add_button(self._gui_wall_button)

        pyxel.run(self.update, self.draw)

    def _set_current_particle(self, particle: Particle):
        self.current_particle = particle

    def _set_pen_size(self, new_size: int):
        if new_size < 1 or new_size > 9:
            return
        self.pen_size = new_size

    def _set_paused(self, paused: bool) -> None:
        self.paused = paused

    def _place_particle(self, particle: Union[Particle, None], center_x: int,
                        center_y: int, radius: int):
        for y in range(-radius, radius):
            for x in range(-radius, radius):
                if (x * x + y * y <= radius * radius):
                    if particle is None:
                        self.canvas_controller.set(
                            center_x + x, center_y + y, None)
                    else:
                        # Check if overwrite is enabled before placing
                        if not self.overwrite and \
                               self.canvas_controller.get(center_x + x, center_y + y) \
                               is not None:
                            continue
                        self.canvas_controller.set(center_x + x, center_y + y,
                                                   particle())

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self._set_paused(not self.paused)

        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.gui.handle_click(pyxel.mouse_x, pyxel.mouse_y)

        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
            self._place_particle(self.current_particle, pyxel.mouse_x -
                                 self.canvas_start_loc[0],
                                 pyxel.mouse_y - self.canvas_start_loc[1],
                                 self.pen_size)

        if pyxel.btn(pyxel.MOUSE_RIGHT_BUTTON):
            self._place_particle(
                None, pyxel.mouse_x - self.canvas_start_loc[0],
                pyxel.mouse_y - self.canvas_start_loc[1], self.pen_size)

        if pyxel.mouse_wheel == 1:
            self._set_pen_size(self.pen_size + 1)
        if pyxel.mouse_wheel == -1:
            self._set_pen_size(self.pen_size - 1)

        self._update_gui_items()
        self._update_particles()

    def _update_gui_items(self):
        self._gui_pen_label.set_value(str(self.pen_size))

        self._gui_sand_button.set_enabled(
            self.current_particle == SandParticle)
        self._gui_wall_button.set_enabled(
            self.current_particle == WallParticle
        )

        self._gui_pause_button.set_hidden(self.paused)
        self._gui_play_button.set_hidden(not self.paused)

    def _update_particles(self):
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

    def draw(self):
        pyxel.cls(1)

        pyxel.text(10, 2, "Sand Game v2", 7)
        pyxel.rect(self.canvas_start_loc[0] - 1, self.canvas_start_loc[1] - 1,
                   self.canvas_width + 2, self.canvas_height + 2, 8)
        pyxel.rect(self.canvas_start_loc[0], self.canvas_start_loc[1],
                   self.canvas_width, self.canvas_height, 0)
        for x in range(self.canvas_width):
            for y in range(self.canvas_height):
                particle = self.canvas_controller.get(x, y)
                if particle is not None:
                    pyxel.rect(
                        x + self.canvas_start_loc[0],
                        y + self.canvas_start_loc[1], 1, 1, particle.color)

        self.gui.draw()
        draw_cursor(self.pen_size - 1, 7)


if __name__ == "__main__":
    SandGame()
