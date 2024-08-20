#!/bin/bash

# Caminho para o diretório onde está o script
cd /home/jpcorso/Documentos/faculdade/6_semestre/ia/trabalhos_praticos_IA/trabalho_4 || { echo "Diretório não encontrado"; exit 1; }

# Comando a ser executado
COMANDO="python3 server.py tttm advsearch/your_agent/tttm_minimax.py advsearch/your_agent/tttm_minimax.py"

# Número de vezes que o comando será executado
NUM_EXECUCOES=50

# Inicializa contadores
player1_vitorias=0
player2_vitorias=0

for ((i=1; i<=NUM_EXECUCOES; i++))
do
    echo "Executando o comando, execução $i..."
    # Executa o comando e pega a última linha da saída
    resultado=$(eval "$COMANDO" | tail -n 4)

    # Checa a última linha para determinar quem venceu
    if echo "$resultado" | grep -q "Player 1 (B - advsearch/your_agent wins!"; then
        ((player1_vitorias++))
    elif echo "$resultado" | grep -q "Player 2 (W - advsearch/randomplayer) wins!"; then
        ((player2_vitorias++))
    fi
done

echo "Player 1 (B - advsearch/your_agent/tttm_minimax.py) venceu $player1_vitorias vezes."
echo "Player 2 (W - advsearch/randomplayer/agent.py) venceu $player2_vitorias vezes."
