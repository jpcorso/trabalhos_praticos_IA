# TRABALHO 1 (turma A): Regressão Linear e TensorFlow 
Arthur Ferreira Ely (00338434), João Pedro Licks Corso (00xxxxxx), Juliana Rodrigues de Vargas (00xxxxxx)

## Implementação Regressão Linear

### Valores iniciais

### MSE


## TensorFlow

### Analise dos datasets
#### MNIST
```Classes:``` 10 (números de 0 a 9)

```Amostras de treino:``` 60.000 imagens

```Amostras de teste:``` 10.000 imagens

```Tamanho das imagens:``` 28 x 28 x 1 (altura x largura x canal de cor, em escala de cinza)

#### Fashion MNIST
```Classes:``` 10 (diversos tipos de roupas e acessórios)

```Amostras de treino:``` 60.000 imagens

```Amostras de teste:``` 10.000 imagens

```Tamanho das imagens:``` 28 x 28 x 1 (altura x largura x canal de cor, em escala de cinza)

#### CIFAR-10
```Classes:``` 10 (objetos do mundo real)

```Amostras de treino:``` 50.000 imagens

```Amostras de teste:``` 10.000 imagens

```Tamanho das imagens:``` 32 x 32 x 3 (altura x largura x canais de cor, em RGB)

#### CIFAR-100
```Classes:``` 100 (subcategorias de objetos do mundo real)

```Amostras de treino:``` 50.000 imagens

```Amostras de teste:``` 10.000 imagens

```Tamanho das imagens:``` 32 x 32 x 3 (altura x largura x canais de cor, em RGB)

### Conclusões redes neurais (Esboço)

**1) Investigue e reflita sobre os fatores que tornam os problemas de classificação de cada dataset mais ou menos complexos em cada dataset. Pense em uma relação de ordem de complexidade/dificuldade dos datasets (os datasets em ordem dos menos complexos/difíceis para os mais complexos/difíceis) e justifique a resposta. O mais importante nesta questão é a investigação e a reflexão e não o fato de a resposta estar precisa.**

- **MNIST**: Mais simples devido à baixa resolução, ausência de cores e padrões claros.

- **Fashion MNIST**: Ligeiramente mais complexo devido à variedade de formas e texturas em comparação com os dígitos do MNIST.

- **CIFAR-10**: Mais complexo do que os anteriores devido à adição de cor e uma variedade maior de objetos, mas ainda gerenciável com arquiteturas de rede neural convolucionais simples.

- **CIFAR-100**: O mais complexo devido ao grande número de classes e subclasses, exigindo modelos mais sofisticados e treinamento mais cuidadoso para obter bons resultados.

Com base nas constatações acima, quanto maior a complexidade do dataset, maior terá que ser a complexidade da rede neural. Em outras palavras, a rede neural terá que ter mais camadas e mais neurônios para conseguir distinguir mais características diferentes entres as imagens. Por exemplo, as características dos números '1' e o número '7' do MNIST são parecidas e não precisam muitos de neurônios para diferencar esses números dos outros. O mesmo acontece com '0', '3', '6', '8' e '9', por todas terem um formato mais circular e se distanciarem das demais. Já na outra ponta, a rede precisa de muitas camadas e neurônios para extrair as muitas características únicas que cada classe tem.

**2) Qual a maior acurácia obtida em cada dataset e quais mudanças fizeram a performance melhorar (ou pior, caso tenha ocorrido piora em relação a alguma performance já avaliada).**


|Dataset| Acurácia | Melhor Desempenho | Pior Desempenho| Mudanças na performance |
| ------------- | ------------- | ------------- | ------------- | ------------- |
|MNIST          |xx,xx%         |X topologia    |X topologia    |Alteramos tal e tal e tal e tal coisa e aí a performance ficou muito diferente que a performance anterior|
|Fashion MNIST  |xx,xx%         |X topologia    |X topologia    |Alteramos tal e tal e tal e tal coisa e aí a performance ficou muito diferente que a performance anterior
|CIFAR-10       |xx,xx%         |X topologia    |X topologia    |Alteramos tal e tal e tal e tal coisa e aí a performance ficou muito diferente que a performance anterior
|CIFAR-100      |xx,xx%         |X topologia    |X topologia    |Alteramos tal e tal e tal e tal coisa e aí a performance ficou muito diferente que a performance anterior



