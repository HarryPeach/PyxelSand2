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
        """Test that the get function
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
