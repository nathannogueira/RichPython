from rich.table import Table
from rich.console import Console

console = Console()

table = Table(title='CADASTRO', show_header=True, style="bold white", header_style="bold white")
table.add_column("Nome", justify="center", style="red")
table.add_column("Idade", justify="center", style="green")
table.add_column("Cidade", justify="center", style="blue")
table.add_column("País", justify="center", style="yellow")

table.add_row("Nathan", "25", "São Paulo", "Brasil")
table.add_row("John", "30", "New York", "EUA")
table.add_row("Jane", "28", "Londres", "Inglaterra")
table.add_row("Bob", "35", "Paris", "França")

console.print(table)
