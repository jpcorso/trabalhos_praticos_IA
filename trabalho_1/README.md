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


- Small network 
      - 32 filtros, janela (3, 3)
      - Janela MaxPooling (2,2)
      - 1 camada de Convolução, 1 camada de MaxPooling, 1 camada de Flatten e 2 camadas Dense. 
- Medium network
      - 2 camadas de Convolução, 2 camadas de MaxPooling, 1 camada de Flatten e 3 camadas Dense. 
- Large network
      - 3 camadas de Convolução, 3 camadas de MaxPooling, 1 camada de Flatten e 4 camadas Dense. 
- Complex network
      - 4 camadas de Convolução, 4 camadas de MaxPooling, 1 camada de Flatten e 5 camadas Dense. 
- Very complex network
      - 4 camadas de Convolução, 4 camadas de MaxPooling, 1 camada de Flatten, Normalização e 3 camadas Dense

```
{'mnist': 
 {'get_small_network': {'time': 80.12140941619873, 'acc': '97.84%'},
  'get_medium_network': {'time': 98.56405687332153, 'acc': '98.85%'},
  'get_large_network': {'time': 125.50758576393127, 'acc': '98.90%'},
  'get_complex_network': {'time': 244.90023851394653, 'acc': '99.30%'},
  'get_very_complex_network': {'time': 237.25664901733398, 'acc': '99.08%'}},
 'fashion_mnist': 
 {'get_small_network': {'time': 76.64522123336792,'acc': '88.94%'},
  'get_medium_network': {'time': 97.64616894721985, 'acc': '89.17%'},
  'get_large_network': {'time': 121.68075728416443, 'acc': '88.76%'},
  'get_complex_network': {'time': 239.64841890335083, 'acc': '91.09%'},
  'get_very_complex_network': {'time': 237.1201777458191, 'acc': '90.82%'}},
```

|Dataset        | Melhor Acurácia | Topologia         | Pior Acurácia| Topologia |
| ------------- | -------------   | -------------     | ------------- | ------------- |
|MNIST          |99,30%           |complex_network    |97,84%         |small_network|
|Fashion MNIST  |91,09%           |complex_network    |88,76%         |large_network|
|CIFAR-10       |xx,xx%           |X topologia        |X topologia    |Alteramos tal e tal e tal e tal coisa e aí a performance ficou muito diferente que a performance anterior
|CIFAR-100      |xx,xx%           |X topologia        |X topologia    |Alteramos tal e tal e tal e tal coisa e aí a performance ficou muito diferente que a performance anterior




