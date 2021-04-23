from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sand_game.canvas import CanvasController

from abc import ABC, abstractmethod
import random


class Particle(ABC):

    def __init__(self) -> None:
        self.updated = False
        self.color = 0

    @abstractmethod
    def update(self, x: int, y: int, canvas: CanvasController) -> None:
        """Called when the particle must update its state

        Args:
            x (int): The current x location of the particle
            y (int): The current y location of the particle
            canvas (CanvasController): The current canvas' controller
        """
        pass

    def fill_space(self, x: int, y: int, canvas: CanvasController) -> None:
        if y == canvas.height - 1:
            return

        if canvas.get(x, y + 1) is None:  # If there is no particle below
            canvas.set(x, y + 1, canvas.get(x, y))
            canvas.set(x, y, None)
            return

        dx_choice = random.choice([-1, 1])

        # Make sure the particles don't leave the canvas
        if (x + dx_choice) >= canvas.width or (x + dx_choice) < 0:
            return

        if canvas.get(x + dx_choice, y) is None:
            canvas.set(x + dx_choice, y, canvas.get(x, y))
            canvas.set(x, y, None)

    def fall(self, x: int, y: int, canvas: CanvasController) -> None:
        """Simulates the particle falling

        Args:
            x (int): The current x-coordinate of the particle
            y (int): The current y-coordinate of the particle
            canvas (CanvasController): The canvas controller which the particle resides
            within
        """
        if y == canvas.height - 1:
            return

        if canvas.get(x, y + 1) is None:  # If there is no particle below
            canvas.set(x, y + 1, canvas.get(x, y))
            canvas.set(x, y, None)
            return

        dx_choice = random.choice([-1, 1])

        # Make sure the particles don't leave the canvas
        if (x + dx_choice) >= canvas.width or (x + dx_choice) < 0:
            return

        # If there is no particle to the sides of the particle
        if canvas.get(x + dx_choice, y + 1) is None:
            canvas.set(x + dx_choice, y + 1, canvas.get(x, y))
            canvas.set(x, y, None)
