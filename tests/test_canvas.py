from __future__ import annotations
from sand_game.particles.FireParticle import FireParticle
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sand_game.particles.Particle import Particle
from expects.matchers.built_in import be_none
from sand_game.canvas import CanvasController
from sand_game.particles.SandParticle import SandParticle
from sand_game.particles.WallParticle import WallParticle

from expects import expect, equal, be


class TestCanvas():
    """Tests the Canvas classes and functions
    """

    def _util_check_only_particle(self, points: list[tuple[int, int]],
                                  chk_particle: Particle, canvas: CanvasController):
        """Check that the given particle exists at the given locations and that every
        other location is empty

        Args:
            points (list[tuple[int, int]]): The points to check
            chk_particle (Particle): The particle to check
            canvas (CanvasController): The canvas to check through
        """
        for x in range(0, canvas.width):
            for y in range(0, canvas.height):
                particle = canvas.get(x, y)
                if (x, y) in points:
                    expect(particle).to(be(chk_particle))
                else:
                    expect(particle).to(be_none)

    def test_canvas_creation(self):
        """Tests that a canvas is successfully created
        """
        canvas = CanvasController(20, 20)

        expect(len(canvas.data)).to(equal(20 * 20))

        for item in canvas.data:
            expect(item).to(be(None))

    def test_canvas_get(self):
        """Test that the get function correctly returns the partciel in a specific
        location
        """
        canvas = CanvasController(3, 3)

        sp = SandParticle()

        canvas.data[4] = sp
        canvas.data[7] = sp

        self._util_check_only_particle([(1, 1), (1, 2)], sp, canvas)

    def test_canvas_set(self):
        """Test the set function correctly sets the particle in a specific location
        """
        canvas = CanvasController(4, 4)

        sp = SandParticle()

        canvas.set(1, 1, sp)
        canvas.set(2, 2, sp)

        self._util_check_only_particle([(1, 1), (2, 2)], sp, canvas)

        canvas.set(1, 1, None)
        canvas.set(2, 2, None)
        canvas.set(3, 1, sp)

        self._util_check_only_particle([(3, 1)], sp, canvas)

    def test_canvas_clear(self):
        """Tests that a canvas is correctly cleared
        """
        canvas = CanvasController(10, 10)

        canvas.set(1, 0, SandParticle())
        canvas.set(9, 1, SandParticle())
        canvas.set(8, 4, SandParticle())
        canvas.set(1, 2, SandParticle())
        canvas.set(3, 1, SandParticle())

        canvas.clear()
        for particle in canvas.data:
            expect(particle).to(be_none)

    def test_save_and_load(_):
        """Test saving and loading to a canvas
        """
        canvas1 = CanvasController(10, 10)
        canvas1.set(1, 0, SandParticle())
        canvas1.set(5, 0, WallParticle())
        canvas1.set(8, 6, SandParticle())
        canvas1.set(5, 7, WallParticle())

        canvas1.save_to_file("TMP.CANVAS")

        canvas2 = CanvasController(5, 5)
        canvas2.load_from_file("TMP.CANVAS")

        expect(canvas1.height).to(equal(canvas2.height))
        expect(canvas1.width).to(equal(canvas2.width))
        expect(len(canvas1.data)).to(equal(len(canvas2.data)))

        # Check all particle types are the same
        for pair in zip(canvas1.data, canvas2.data):
            particle1, particle2 = pair

            if particle1 is None:
                expect(particle2).to(be_none)
                continue

            expect(type(particle1)).to(be(type(particle2)))

    def test_load_particle_data(_):
        """Test particle data is persisted after load
        """
        canvas1 = CanvasController(10, 10)
        fp = FireParticle()
        fp.max_tick = 5001
        canvas1.set(1, 0, fp)
        canvas1.save_to_file("TMP.CANVAS")

        canvas2 = CanvasController(5, 5)
        canvas2.load_from_file("TMP.CANVAS")
        expect(canvas2.get(1, 0).max_tick).to(equal(5001))
