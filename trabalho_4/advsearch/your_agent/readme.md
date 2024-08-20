Arthur Ferreira Ely (00338434)
João Pedro Licks Corso (00337569)
Julina Rodrigues de Vargas (00337553)

Nenhuma biblioteca adicional precisa ser instalada.

Resultados:

Tic-Tac-Toe

(i) O minimax sempre ganha do randomplayer?
R.: Testamos 50 vezes com o nosso agente sendo o primeiro jogador e 50 vezes com o minimax sendo o seugndo. Jogando como primeiro jogador,
obteve 28 vitórias e 22 derrotas. Já como segundo jogador obteve 28 vitórias e 10 derrotas.

(ii) O minimax sempre empata consigo mesmo?
R.: Testamos 150 vezes e ele sempre empata consigo mesmo.

(iii) O minimax não perde para você, quando você usa a sua melhor estratégia?
R.: Não perde. Sempre acaba empatando.

Othello

Heurística Customizada

Essa heurística considera não só a contagem simples de peças, mas também fatores estratégicos como a ocupação dos cantos e a estabilidade das peças, o que torna a avaliação mais robusta e alinhada com a complexidade estratégica de Othello.

Partidas:
(15) Contagem de peças       0 x 1   Valor posicional       (49)
(43) Valor posicional        1 x 0   Contagem de peças      (21)
(54) Contagem de peças       1 x 0   Heurística customizada (10)
(52) Heurística customizada  1 x 0   Contagem de peças      (12)
(43) Valor posicional        1 x 0   Heurística customizada (21)
(17) Heurística customizada  0 x 1   Valor posicional       (47)

(ii) Observe e relate qual implementação foi a mais bem-sucedida.
R.: Dos 9 testes, o jogador que começou jogando ganhou em 8. Apenas no confronto custom x mask, a heurística mask conseguiu empatar mesmo sendo o segundo jogador.

(iii) Reflita sobre o que pode ter tornado cada heurística melhor ou pior, em termos de performance.
R.: O mask parece ser um algoritmo um pouco mais eficiente, porque não só leva em consideração o número de peças no tabuleiro, mas também dá pontos para suas posições.

Feedback:
O trabalho foi de fácil implementação. Utilizamos o ChatGPT, o GitHub Copilot e o Gemini para o apoio no desenvolvimento do código, além dos conceitos aprendidos na disciplina.