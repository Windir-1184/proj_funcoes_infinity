def criar_tarefa(n):
    tarefas = {}
    for i in range(n):
        tarefas.update({
            f"Nome Tarefa {i+1}": input(f"Informe o nome da tarefa {i+1}: "),
            f"Descrição Tarefa {i+1}": input(f"Informe a Descrição da tarefa {i+1}: "),
            f"Prioridade da Tarefa {i+1}": input(f"Informe a Prioridade da tarefa {i+1}: "),
            f"Categoria da Tarefa {i+1}": input(f"Informe a Categoria da tarefa {i+1}: ")
        })
    return tarefas

print(criar_tarefa(2))