from textual import events
from rich.table import Table
from rich.style import Style
from textual.widgets import ScrollView, Static

class CustomInputs(Static):
    """Override the default Header for styling"""

    def __init__(self, *inputs) -> None:
        super().__init__()
        self.inputs = inputs

    def render(self) -> Table:
        header_table = Table.grid(padding=(0,1), expand=True)
        header_table.style = Style(color="white", bgcolor="rgb(98,98,98)")
        header_table.add_column(justify="left", ratio=0, width=8)
        for input in self.inputs:
            header_table.add_row(
                self.input
            )

        return header_table