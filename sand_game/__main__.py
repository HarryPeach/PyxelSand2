from sand_game.particles.SandParticle import SandParticle
from sand_game.particles.WallParticle import WallParticle
from sand_game.canvas import CanvasController
from sand_game.draw_utils import draw_cursor
from sand_game.gui import draw_menu
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

    def update(self):
        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
            self.canvas_controller.set(
                pyxel.mouse_x - self.canvas_start_loc[0],
                pyxel.mouse_y - self.canvas_start_loc[1], SandParticle())

        if pyxel.btn(pyxel.MOUSE_RIGHT_BUTTON):
            self.canvas_controller.set(
                pyxel.mouse_x - self.canvas_start_loc[0],
                pyxel.mouse_y - self.canvas_start_loc[1], None)

        for x in range(self.canvas_width):
            for y in range(self.canvas_height):
                particle = self.canvas_controller.get(x, y)
                if particle is None:
                    continue

                if particle.updated:
                    continue

                particle.update(x, y, self.canvas_controller)

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

        draw_cursor(7)


if __name__ == "__main__":
    SandGame()
