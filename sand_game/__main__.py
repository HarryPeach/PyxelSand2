from sand_game.particles.SandParticle import SandParticle
from sand_game.particles.WallParticle import WallParticle
from sand_game.particles.Particle import Particle
from sand_game.canvas import CanvasController
from sand_game.draw_utils import draw_cursor
from sand_game.gui import draw_menu
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

        self.pen_size = 1

        pyxel.run(self.update, self.draw)

    def _place_particle(self, particle: Union[Particle, None], center_x: int,
                        center_y: int, radius: int):
        for y in range(-radius, radius):
            for x in range(-radius, radius):
                if (x * x + y * y <= radius * radius):
                    if particle is None:
                        self.canvas_controller.set(center_x + x, center_y + y, None)
                    else:
                        self.canvas_controller.set(center_x + x, center_y + y,
                                                   particle())

    def update(self):
        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
            self._place_particle(SandParticle, pyxel.mouse_x -
                                 self.canvas_start_loc[0],
                                 pyxel.mouse_y - self.canvas_start_loc[1],
                                 self.pen_size)

        if pyxel.btn(pyxel.MOUSE_RIGHT_BUTTON):
            self._place_particle(
                None, pyxel.mouse_x - self.canvas_start_loc[0],
                pyxel.mouse_y - self.canvas_start_loc[1], self.pen_size)

        if pyxel.mouse_wheel == 1 and self.pen_size < 9:
            self.pen_size = self.pen_size + 1
        if pyxel.mouse_wheel == -1 and self.pen_size > 1:
            self.pen_size = self.pen_size - 1

        self._update_particles()

    def _update_particles(self):
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
        draw_menu(self, 114, 10)

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

        draw_cursor(self.pen_size - 1, 7)


if __name__ == "__main__":
    SandGame()
