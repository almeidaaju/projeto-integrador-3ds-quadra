from datetime import datetime, time


horarios_manha = [
    ("7:15", "8:05"),
    ("8:05", "8:55"),
    ("8:55", "9:45"),
    ("10:05", "10:50"),
    ("10:50", "11:35"),
    ("11:35", "12:25"),
]

horarios_tarde = [
    ("13:10", "14:05"),
    ("14:05", "14:55"),  
    ("14:55", "15:45"),
    ("15:45", "16:40"),
    ("16:40", "17:30"),
    ("17:30", "18:10"),
]


def converter_para_time(string_hora):
  """Converte 'H:MM' para objeto time do Python"""
  partes = string_hora.strip().split(":")
  return time(int(partes[0]), int(partes[1]))


def calcular_duracao(inicio, fim):
  """Calcula a duração em minutos entre dois objetos time"""
  t_inicio = datetime.combine(datetime.today(), inicio)
  t_fim = datetime.combine(datetime.today(), fim)
  diferenca = t_fim - t_inicio
  return int(diferenca.total_seconds() / 60)


def verificar_aula_atual(lista_horarios, periodo_nome):
  """Verifica se o horário atual está dentro de alguma aula"""
  agora = datetime.now().time()
 

  print(f"\n--- Verificando Período: {periodo_nome} ---")
  encontrou = False

  for i, (h_inicio_str, h_fim_str) in enumerate(lista_horarios, 1):
    inicio = converter_para_time(h_inicio_str)
    fim = converter_para_time(h_fim_str)
    duracao = calcular_duracao(inicio, fim)

    status = ""
    if inicio <= agora <= fim:
      status = " 🔴 [AULA ATUAL ROLANDO]"
      encontrou = True

    print(
        f"Aula {i:02d}: {h_inicio_str} às {h_fim_str} "
        f"(Duração: {duracao} min){status}"
    )

  return encontrou



if __name__ == "__main__":
  print(f"Horário atual do sistema: {datetime.now().strftime('%H:%M:%S')}")


  verificar_aula_atual(horarios_manha, "Manhã")

  
  verificar_aula_atual(horarios_tarde, "Tarde")