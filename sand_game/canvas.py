"""Classes and functions related to the game canvas
"""
from __future__ import annotations
from typing import Union

from sand_game.particles.Particle import Particle


class CanvasController():
    """The main controller for the game canvas, controlling the location of all
    particles
    """
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.data = [None] * width * height

    def clear(self):
        """Clears the canvas
        """
        for i in range(0, len(self.data)):
            self.data[i] = None

    def set(self, x: int, y: int, particle: Union[Particle, None]) -> None:
        """Sets the particle at the current location

        Args:
            x (int): The x-coordinate of the canvas
            y (int): The y-coordinate of the canvas
            particle (Union[Particle, None]): The particle to set, or NoneType to clear
        """
        if x > self.width or x < 0:
            return
        if y > self.height - 1 or y < 0:
            return

        self.data[(x % self.width) + (y * self.width)] = particle

    def get(self, x: int, y: int) -> Union[Particle, None]:
        """Gets the particle at the current location

        Args:
            x (int): the x-coordinate of the canvas
            y (int): the y-coordinate of the canvas

        Returns:
            Particle | None: The particle as the location or NoneType if location is
            empty
        """
        if x > self.width or x < 0:
            return None
        if y > self.height - 1 or y < 0:
            return None

        return self.data[(x % self.width) + (y * self.width)]
