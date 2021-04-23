from typing import Callable
import pyxel


class TexturedButton():
    """A GUI component that represents a button which has a texture from the resource
    file
    """
    def __init__(self, action: Callable, x: int, y: int, u: int, v: int, width: int,
                 height: int, tooltip: str = "", enabled: bool = False,
                 hidden: bool = False) -> None:
        """Create the button

        Args:
            action (Callable): The callback for when the button is pressed
            x (int): The start x-coordinate to draw from
            y (int): The start y-coordinate to draw from
            u (int): The u-value of the texture
            v (int): The v-value of the texture
            width (int): The width of the button
            height (int): The height of the button
            tooltip (str): The tooltip, describing the button
            enabled (bool, optional): Whether the button is enabled. Defaults to False.
            hidden (bool, optional): Whether the button should be rendered and checked
            for clicks. Defaults to False.
        """
        self.action = action
        self.x = x
        self.y = y
        self.u = u
        self.v = v
        self.width = width
        self.height = height
        self.tooltip = tooltip
        self.enabled = enabled
        self.hidden = hidden

    def set_enabled(self, enabled: bool) -> None:
        self.enabled = enabled

    def set_hidden(self, hidden: bool) -> None:
        self.hidden = hidden


class Label():
    """A GUI component that represents a string to be drawn
    """
    def __init__(self, value: str, x: int, y: int, color: int) -> None:
        """Create the Label

        Args:
            value (str): The string to render
            x (int): The start x-coordinate of the Label
            y (int): The start y-coordinate of the Label
            color (int): The color to draw the Label
        """
        self.value = value
        self.x = x
        self.y = y
        self.color = color

    def set_value(self, value: str) -> None:
        self.value = value


class Gui():
    """Manages the GUI including drawing, and object management
    """

    def __init__(self, start_x: int, start_y: int) -> None:
        """Creates the GUI object

        Args:
            start_x (int): The start x-coordinate to draw the GUI
            start_y (int): The start y-coordinate to draw the GUI
        """
        self.start_x = start_x
        self.start_y = start_y
        self.texts: list[Label] = []
        self.buttons: list[TexturedButton] = []

    def draw(self) -> None:
        """Draw all UI elements assigned to the GUI object
        """
        self._draw_buttons()
        self._draw_texts()

    def _draw_texts(self) -> None:
        for text in self.texts:
            pyxel.text(self.start_x + text.x, self.start_y + text.y,
                       text.value, text.color)

    def _draw_buttons(self) -> None:
        for button in self.buttons:
            if button.hidden:
                continue

            if not button.enabled:
                pyxel.blt(self.start_x + button.x, self.start_y + button.y, 0, button.u,
                          button.v, button.width, button.height)
            else:
                pyxel.blt(self.start_x + button.x, self.start_y + button.y, 0,
                          button.u + 16, button.v, button.width, button.height)

    def add_button(self, button: TexturedButton) -> None:
        """Add a button object to the GUI renderer

        Args:
            button (TexturedButton): The button object to be added
        """
        self.buttons.append(button)

    def add_label(self, text: Label) -> None:
        """Add a text object to the GUI renderer

        Args:
            text (Label): The label object to be added
        """
        self.texts.append(text)

    def handle_hover(self, x: int, y: int) -> None:
        """Handles hover events and draws tooltips if necessary

        Args:
            x (int): The x-coordinate of the mouse
            y (int): The y-coordinate of the mouse
        """
        for button in self.buttons:
            if button.hidden:
                continue

            start_x: int = button.x + self.start_x
            start_y: int = button.y + self.start_y
            if (x >= start_x) and (x < start_x + button.width) and (y >= start_y) \
               and (y < start_y + button.height):
                pyxel.text(self.start_x, self.start_y + 100, button.tooltip, 7)

    def handle_click(self, x: int, y: int) -> None:
        """Handles clicks and activates buttons if required

        Args:
            x (int): The x-coordinate of a click
            y (int): The y-coordinate of a click
        """
        for button in self.buttons:
            if button.hidden:
                continue

            start_x: int = button.x + self.start_x
            start_y: int = button.y + self.start_y
            if (x >= start_x) and (x < start_x + button.width) and (y >= start_y) \
               and (y < start_y + button.height):
                button.action()
