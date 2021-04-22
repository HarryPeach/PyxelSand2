from expects.matchers.built_in import be_none
from sand_game.canvas import CanvasController
from sand_game.particles.SandParticle import SandParticle

from expects import expect, equal, be


class TestCanvas():
    """Tests the Canvas classes and functions
    """

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

        for x in range(0, 3):
            for y in range(0, 3):
                particle = canvas.get(x, y)
                if (x == 1 and y == 1) or (x == 1 and y == 2):
                    expect(particle).to(be(sp))
                else:
                    expect(particle).to(be_none)

    # TODO (Harry): Refactor - Cognitive Complexity
    def test_canvas_set(self):
        """Test the set function correctly sets the particle in a specific location
        """
        canvas = CanvasController(4, 4)

        sp = SandParticle()

        canvas.set(1, 1, sp)
        canvas.set(2, 2, sp)

        for x in range(0, 4):
            for y in range(0, 4):
                particle = canvas.get(x, y)
                if (x, y) == (1, 1) or (x, y) == (2, 2):
                    expect(particle).to(be(sp))
                else:
                    expect(particle).to(be_none)

        canvas.set(1, 1, None)
        canvas.set(2, 2, None)
        canvas.set(3, 1, sp)

        for x in range(0, 4):
            for y in range(0, 4):
                particle = canvas.get(x, y)
                if (x == 3 and y == 1):
                    expect(particle).to(be(sp))
                else:
                    expect(particle).to(be_none)

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
