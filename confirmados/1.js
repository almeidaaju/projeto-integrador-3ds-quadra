const janela = document.getElementById('janelaAgendamento');
const lista = document.getElementById('listaHorarios');


function mostrarJanela(abrir) {
  janela.style.display = abrir ? 'flex' : 'none';
}


function adicionarHorario(evento) {
  evento.preventDefault();

  const data = document.getElementById('campoData').value;
  const horario = document.getElementById('campoHorario').value;
  const local = document.getElementById('campoLocal').value;
  const disciplina = document.getElementById('campoDisciplina').value;

  const novoCartao = document.createElement('div');
  novoCartao.className = 'cartao';
  novoCartao.innerHTML = `
    <div class="linha-cartao">
      <span>${data}</span>
      <span>Horário: ${horario}</span>
    </div>
    <div><strong>Local:</strong> ${local}</div>
    <div><strong>Disciplina:</strong> ${disciplina}</div>
    <div class="status"><i class="fa-solid fa-circle-check"></i> Confirmado</div>
  `;

  lista.appendChild(novoCartao);
  evento.target.reset();
  mostrarJanela(false);
}