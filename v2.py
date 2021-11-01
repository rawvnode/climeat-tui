from rich.table import Table
from rich.markdown import Markdown
from rich.style import Style
from textual import events
from textual.app import App
from textual.widgets import Footer, ScrollView
from textual_inputs import IntegerInput, TextInput
from textual.reactive import Reactive

from climeat import get_city
from header import CustomHeader

import json

class Climeat(App):

    current_index: Reactive[int] = Reactive(-1)

    async def on_load(self) -> None:
        """Key Bindings"""
        await self.bind("q", "quit", "Quit")
        await self.bind("enter", "submit", "Submit")

    async def on_mount(self) -> None:
        """Mount"""

        input_table = Table.grid(padding=(0,1), expand=True)
        input_table.style = Style(color="white", bgcolor="rgb(98,98,98)")
        input_table.add_column(justify="left", ratio=0, width=8)

        self.input = TextInput(
            name="city_name",
            placeholder="enter the city name...",
            title="City Name"
        )
        self.output = ScrollView()

        input_table.add_row(self.input)

        self.header = CustomHeader()
        await self.view.dock(self.header, edge="top")
        await self.view.dock(Footer(), edge="bottom")
        await self.view.dock(self.input, edge="left", size=40)
        await self.view.dock(self.output, edge="left")

    async def action_submit(self) -> None:
        """Search city"""
        city = get_city(self.input.value)
        await self.output.update(json.dumps(city))

if __name__ == "__main__":
    Climeat.run(title="Climeat", log="v2.log")