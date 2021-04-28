"""Classes and functions related to the game canvas
"""
from __future__ import annotations
from typing import Union

from sand_game.particles.Particle import Particle

import json
import zlib


class CanvasController():
    """The main controller for the game canvas, controlling the location of all
    particles
    """
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.data = [None] * width * height

    def clear(self) -> None:
        """Clears the canvas
        """
        for i in range(0, len(self.data)):
            self.data[i] = None

    def _serialize(self) -> dict:
        """Converts the object into a JSON dict

        Returns:
            str: The JSON form of the canvas
        """
        serial_obj = {
            "width": self.width,
            "height": self.height,
        }
        particles = []
        particle: Particle
        for particle in self.data:
            if particle is None:
                particles.append(particle)
                continue

            particles.append(particle._serialize())

        serial_obj["particles"] = particles
        return serial_obj

    @staticmethod
    def _from_serialized(serial_obj: dict) -> CanvasController:
        """Create a new CanvasController object from a serialized dict

        Args:
            serial_obj (dict): The serialized dict to create from

        Returns:
            CanvasController: The newly created object
        """
        new_canvas = CanvasController(serial_obj["width"], serial_obj["height"])
        for i, particle_data in enumerate(serial_obj["particles"]):
            if particle_data is None:
                new_canvas.data[i] = None
                continue

            new_particle = Particle._from_serialized(particle_data)
            new_canvas.data[i] = new_particle
        return new_canvas

    def save_to_file(self, filename: str) -> None:
        """Saves the canvas to a file

        Args:
            filename (str): The file to save the canvas to
        """
        with open(filename, "wb") as f:
            json_str = json.dumps(self._serialize())
            json_str_compr = zlib.compress(json_str.encode("utf-8"))
            f.write(json_str_compr)

    @staticmethod
    def load_from_file(filename: str) -> CanvasController:
        """Loads the canvas from a file

        Args:
            filename (str): The file to load the canvas from
        """
        with open(filename, "rb") as f:
            decomp = zlib.decompress(f.read())
            serial_obj = json.loads(decomp.decode("utf-8"))
            return CanvasController._from_serialized(serial_obj)

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
