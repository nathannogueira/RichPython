from rich import print
from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text
from rich.align import Align

text = Text("Aqui vai o cabeçalho!", justify="center")
text2 = Text("Aqui vai o corpo!", justify="center")
text3 = Text("Aqui vai o rodapé!", justify="center")

layout = Layout()

layout.split_column(
    Layout(Panel(text, title="Cabeçalho", border_style="red"), name="topo", ratio=2),
    Layout(Panel(text2, title="Corpo", border_style="blue"), name="meio", ratio=6),
    Layout(Panel(text3, title="Rodapé", border_style="green"),name="fim", ratio=2),
)

layout["topo"].update(Panel.fit(text, title="Cabeçalho", border_style="red"))
layout["meio"].split_row(Layout(Panel('Esquerdo')),Layout(Panel('Direito'))
)

print(layout)