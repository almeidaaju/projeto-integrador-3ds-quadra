     function mostrarJanela(abrir) {
      document.getElementById('janelaAgendamento').style.display = abrir ? 'flex' : 'none';
    {"}"}
    }

    function adicionarHorario(evento) {
      evento.preventDefault();

      var data = document.getElementById('campoData').value;
      var horario = document.getElementById('campoHorario').value;
      var local = document.getElementById('campoLocal').value;
      var disciplina = document.getElementById('campoDisciplina').value;

      var novoCartao = document.createElement('div');
      novoCartao.className = 'cartao';
      novoCartao.innerHTML = 
        '<div class="linha-cartao">' +
          '<span>' + data + '</span>' +
          '<span>' + horario + '</span>' +
        '</div>' +
        '<p><span>Local:</span> ' + local + '</p>' +
        '<p><span>Disciplina:</span> ' + disciplina + '</p>' +
        '<div class="status"><i class="fa-solid fa-circle-check"></i> Confirmado</div>';

      var lista = document.getElementById('listaHorarios');
      lista.appendChild(novoCartao);
      
      evento.target.reset();
      mostrarJanela(false);
      lista.scrollTop = lista.scrollHeight;
    }
