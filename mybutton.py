from rich.console import RenderableType
from textual.reactive import Reactive
from textual.widgets import Button, ButtonPressed

class MyButton(Button):

    DARK = "white on rgb(51,51,51)"
    LIGHT = "black on rgb(165,165,165)"
    YELLOW = "white on rgb(255,159,7)"

    mouse_over = Reactive(False)

    def __init__(
        self,
        label: RenderableType,
        name: str = None
    ):
        super().__init__(label=label, name=name, style=self.DARK)


    def on_enter(self) -> None:
        self.mouse_over = True
        self.button_style = self.LIGHT

    def on_leave(self) -> None:
        self.mouse_over = False
        self.button_style = self.DARK
