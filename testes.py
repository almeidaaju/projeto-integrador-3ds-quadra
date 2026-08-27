
agendamentos = [
    {
        "data": "Hoje, 17 de Junho",
        "horario": "14:05 - 14:55",
        "local": "Quadra coberta",
        "disciplina": "Ed.Física (8A)",
    },
    {
        "data": "Amanhã, 18 de Junho",
        "horario": "08:55 - 09:45",
        "local": "Quadra coberta",
        "disciplina": "Ed.Física (3T - Marcelo)",
    },
]


def listar_horarios(lista):
    print("\n--- HORÁRIOS CONFIRMADOS ---")
    if not lista:
        print("Nenhum agendamento encontrado.")
        return

    for item in lista:
        print(f"\n[{item['data']}] {item['horario']}")
        print(f"Local: {item['local']}")
        print(f"Disciplina: {item['disciplina']}")
        print("Status: Confirmado")


def buscar_horario():
    termo = input("\nDigite o termo de busca: ").lower()
    resultados = []

    for item in agendamentos:
        texto_completo = (
            f"{item['data']} {item['local']} {item['disciplina']}".lower()
        )
        if termo in texto_completo:
            resultados.append(item)

    listar_horarios(resultados)


def adicionar_horario():
    print("\n--- NOVO AGENDAMENTO ---")
    data = input("Data: ")
    horario = input("Horário: ")
    local = input("Local: ")
    disciplina = input("Disciplina: ")

    novo = {
        "data": data,
        "horario": horario,
        "local": local,
        "disciplina": disciplina,
    }

    agendamentos.append(novo)
    print("Agendamento salvo com sucesso!")


#
while True:
    print("\n1. Ver todos os horários")
    print("2. Buscar horário")
    print("3. Adicionar horário")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listar_horarios(agendamentos)
    elif opcao == "2":
        buscar_horario()
    elif opcao == "3":
        adicionar_horario()
    elif opcao == "4":
        break
    else:
        print("Opção inválida.")