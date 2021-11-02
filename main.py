from typing import Text
from rich.console import Console, ConsoleOptions, RenderableType
from rich.markdown import Markdown
from rich.panel import Panel
from rich.table import Table
from rich.style import StyleType

from textual import events
from textual.app import App
from textual.widgets import Button, ButtonPressed, Header, Footer, ScrollView

from textual_inputs import IntegerInput, TextInput

from mybutton import MyButton
from climeat import get_cities, get_city, get_meat_overconsumption, get_meat_per_capita

import json


class MyApp(App):
    """An example of a very simple Textual App"""

    async def on_load(self, event: events.Load) -> None:
        """Bind keys with the app loads (but before entering application mode)"""
        await self.bind("c", "clear_results", "Clear")
        await self.bind("q", "quit", "Quit")

    async def on_mount(self, event: events.Mount) -> None:
        """Create and dock the widgets."""

        self.results = ScrollView()

        await self.view.dock(Header(), edge="top")
        await self.view.dock(Footer(), edge="bottom")

        grid = await self.view.dock_grid()

        grid.set_gap(2, 2)
        grid.set_gutter(1)
        grid.set_align("center", "center")

        grid.add_column("left", size=30)
        grid.add_column("right")
        grid.add_row(name="top")
        grid.add_row(name="middle")
        grid.add_row(name="bottom")
       
        grid.add_areas(
            story_open="left,top",
            moscow="left,middle",
            cities="left,bottom",
            results="right,top-start|bottom-end"
        )

        self.story_button = MyButton(label="Story", name="Story")
        self.city_button = MyButton(label="City", name="Moscow")
        self.cities_button = MyButton(label="Meat Over Consumption", name="Meat")

        grid.place(
            story_open=self.story_button,
            moscow=self.city_button,
            cities=self.cities_button,
            results=self.results
        )


    async def handle_button_pressed(self, message: ButtonPressed) -> None:
        """A message sent by the button widget"""

        assert isinstance(message.sender, Button)
        button_name = message.sender.name

        import time
        if button_name == "Meat":
            start = time.time()
            cities = get_meat_overconsumption()
            end = time.time()
            
            cities_table = Table(show_header=True, header_style="bold green", caption=f"retrieved with ❤️ in {end-start} seconds")
            for k in cities[0].keys():
                cities_table.add_column(k)
            
            for c in cities:
                l = [str(v) for v in c.values()]
                cities_table.add_row(*l, end_section=True)

            await self.results.update(cities_table) #json.dumps(cities, indent=2))
        elif button_name == "Moscow":
            moscow = get_city("Moscow")

            # city_table = Table(show_header=True, header_style="bold magenta")
            # for k in moscow.keys():
            #     city_table.add_column(k)
            
            # l = [str(v) for v in moscow.values()]
            # city_table.add_row(*l, end_section=True)

            await self.results.update(json.dumps(moscow, indent=2))
        elif button_name == "Story":
            with open("narrative.md", "rt") as fh:
                md = Markdown(fh.read(), hyperlinks=True)
                await self.results.update(md)

    async def action_clear_results(self):
        """Clear the api results screen"""

        await self.results.update("")

MyApp.run(title="Climeat", log="textual.log")