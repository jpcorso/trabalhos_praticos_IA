#!/bin/bash

# Caminho para o diretório onde estão os scripts
cd /home/jpcorso/Documentos/faculdade/6_semestre/ia/trabalhos_praticos_IA/trabalho_4 || { echo "Diretório não encontrado"; exit 1; }

# Lista de comandos a serem executados
COMANDOS=(
    "python server.py othello advsearch/your_agent/othello_minimax_count.py advsearch/your_agent/othello_minimax_mask.py"
    "python server.py othello advsearch/your_agent/othello_minimax_mask.py advsearch/your_agent/othello_minimax_count.py"
    "python server.py othello advsearch/your_agent/othello_minimax_count.py advsearch/your_agent/othello_minimax_custom.py"
    "python server.py othello advsearch/your_agent/othello_minimax_custom.py advsearch/your_agent/othello_minimax_count.py"
    "python server.py othello advsearch/your_agent/othello_minimax_mask.py advsearch/your_agent/othello_minimax_custom.py"
    "python server.py othello advsearch/your_agent/othello_minimax_custom.py advsearch/your_agent/othello_minimax_mask.py"
)

# Número de vezes que cada comando será executado
NUM_EXECUCOES=1

# Inicializa os contadores
declare -A vitorias_player1
declare -A vitorias_player2

# Inicializa os contadores para cada comando
for comando in "${COMANDOS[@]}"; do
    vitorias_player1["$comando"]=0
    vitorias_player2["$comando"]=0
done

for ((i=1; i<=NUM_EXECUCOES; i++))
do
    for comando in "${COMANDOS[@]}"; do
        echo "Executando o comando: \"$comando\", execução $i..."
        # Executa o comando e pega a última linha da saída
        resultado=$(eval "$comando" | tail -n 10)

        # Checa a saída para determinar quem venceu
        if echo "$resultado" | grep -q "Player 1.*wins!"; then
            vitorias_player1["$comando"]=$(( ${vitorias_player1["$comando"]} + 1 ))
        elif echo "$resultado" | grep -q "Player 2.*wins!"; then
            vitorias_player2["$comando"]=$(( ${vitorias_player2["$comando"]} + 1 ))
        fi
    done
done

# Exibe o resultado das vitórias
for comando in "${COMANDOS[@]}"; do
    echo "Comando \"$comando\" venceu ${vitorias_player1["$comando"]} vezes para Player 1 e ${vitorias_player2["$comando"]} vezes para Player 2."
done
