from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sand_game.canvas import CanvasController

from abc import ABC, abstractmethod
import random


class Particle(ABC):

    def __init__(self, color: int, burntime: int = -1, updated: bool = False) -> None:
        self.updated = updated
        self.burntime = burntime
        self.color = color

    @abstractmethod
    def update(self, x: int, y: int, canvas: CanvasController) -> None:
        """Called when the particle must update its state

        Args:
            x (int): The current x location of the particle
            y (int): The current y location of the particle
            canvas (CanvasController): The current canvas' controller
        """
        self.updated = True

    def fill_space(self, x: int, y: int, canvas: CanvasController) -> None:
        self.fall(x, y, canvas, fill_space=True)

    def fall(self, x: int, y: int, canvas: CanvasController, fill_space=False,
             direction: int = 1) -> None:
        """Simulates the particle falling

        Args:
            x (int): The current x-coordinate of the particle
            y (int): The current y-coordinate of the particle
            canvas (CanvasController): The canvas controller which the particle resides
            within
            fill_space (bool): Whether the particle should fill the available space
            direction (int): The direction in which the particle should fall, 1 for down
            and -1 for up
        """
        if y == canvas.height - direction:
            return

        if canvas.get(x, y + direction) is None:  # If there is no particle below
            canvas.set(x, y + direction, canvas.get(x, y))
            canvas.set(x, y, None)
            return

        dx_choice = random.choice([-1, 1])

        # Make sure the particles don't leave the canvas
        if (x + dx_choice) >= canvas.width or (x + dx_choice) < 0:
            return

        dy = 0 if fill_space else direction
        # If there is no particle to the sides of the particle
        if canvas.get(x + dx_choice, y + dy) is None:
            canvas.set(x + dx_choice, y + dy, canvas.get(x, y))
            canvas.set(x, y, None)
