from rich.progress import track
from time import sleep

for tarefa in track(range(30), 'Progresso:'):
    sleep(0.5)
    print(f'Processando tarefa {tarefa}...')