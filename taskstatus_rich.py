from rich.console import Console
from time import sleep

console = Console()

with console.status('Processando...') as status:
    for tarefa in range(20):
        sleep(0.5)
        status.update(f'Processando tarefa {tarefa}...')
        print(tarefa)