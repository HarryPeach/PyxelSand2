from sand_game.particles.SandParticle import SandParticle
from sand_game.canvas import CanvasController
import pyxel
import time


class SandGame:
    def __init__(self):
        pyxel.init(160, 120)

        self.canvas_width = 64
        self.canvas_height = 64
        self.canvas_start_location = (10, 10)
        self.canvas_controller = CanvasController(
            self.canvas_width, self.canvas_height)

        # TODO (Harry): Remove debug sand particle
        for i in range(0, 15):
            self.canvas_controller.set(32, i, SandParticle())

        pyxel.run(self.update, self.draw)

    def update(self):
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
        pyxel.text(10, 2, "Debug Canvas: ", 7)
        pyxel.rect(self.canvas_start_location[0] - 1, self.canvas_start_location[1] - 1,
                   self.canvas_width + 2, self.canvas_height + 2, 8)
        pyxel.rect(self.canvas_start_location[0], self.canvas_start_location[1],
                   self.canvas_width, self.canvas_height, 0)
        for x in range(self.canvas_width):
            for y in range(self.canvas_height):
                particle = self.canvas_controller.get(x, y)
                if particle is not None:
                    pyxel.rect(
                        x + self.canvas_start_location[0],
                        y + self.canvas_start_location[1], 1, 1, particle.color)


if __name__ == "__main__":
    SandGame()
