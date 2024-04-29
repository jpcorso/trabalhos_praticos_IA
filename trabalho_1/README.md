# TRABALHO 1 (turma A): Regressão Linear e TensorFlow 
Arthur Ferreira Ely (00338434), João Pedro Licks Corso (00xxxxxx), Juliana Rodrigues de Vargas (00337553)

## Implementação Regressão Linear

### Valores iniciais
      - b:5
      - w: 1
      - alpha: 0.01
      - iterations: 100
### MSE
      8,73

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


- Small/Simple network 

      - Camada Convolucional:
            Tamanho da janela: (3, 3)
            Número de filtros: 32
            Função de ativação: ReLU
  
      - Camada de Pooling (MaxPooling2D):
            Tamanho da janela: (2, 2)
  
      - Camada de Achatamento (Flatten):
            Não há parâmetros a serem ajustados.
  
      - Camada Densa (Fully Connected):
            Número de neurônios: 64
            Função de ativação: ReLU
  
      - Camada de Saída (Densa):
            Número de neurônios: Número de classes
            Função de ativação: Softmax (para classificação multiclasse)
  
- Medium network

 ```
     - Camada Convolucional 1:
            Tamanho da janela: (3, 3)
            Número de filtros: 32
            Função de ativação: ReLU
     - Camada de Pooling 1 (MaxPooling2D):
            Tamanho da janela: (2, 2)
     - Camada Convolucional 2:
            Tamanho da janela: (3, 3)
            Número de filtros: 64
            Função de ativação: ReLU
     - Camada de Pooling 2 (MaxPooling2D):
            Tamanho da janela: (2, 2)
     - Camada de Achatamento (Flatten):
            Não há parâmetros a serem ajustados.
     - Camada Densa 1 (Fully Connected):
            Número de neurônios: 128
            Função de ativação: ReLU
     - Camada Densa 2 (Fully Connected):
            Número de neurônios: 64
            Função de ativação: ReLU
     - Camada de Saída (Densa):
            Número de neurônios: Número de classes
            Função de ativação: Softmax (para classificação multiclasse)
```

- Large network
```
      - Camada de Pooling 1 (MaxPooling2D):
            Tamanho da janela: (2, 2)
      - Camada Convolucional 2: 
            Tamanho da janela: (3, 3)
            Número de filtros: 64
            Função de ativação: ReLU
      - Camada de Pooling 2 (MaxPooling2D):
            Tamanho da janela: (2, 2)
      - Camada Convolucional 3: 
            Tamanho da janela: (3, 3)
            Número de filtros: 128
            Função de ativação: ReLU
            Padding: same
      - Camada de Pooling 3 (MaxPooling2D):
            Tamanho da janela: (2, 2)
      - Camada de Achatamento (Flatten):
            Não há parâmetros a serem ajustados.
      - Camada Densa 1 (Fully Connected):
            Número de neurônios: 256
            Função de ativação: ReLU
      - Camada Densa 2 (Fully Connected):
            Número de neurônios: 128
            Função de ativação: ReLU
      - Camada Densa 3 (Fully Connected):
            Número de neurônios: 64
            Função de ativação: ReLU
      - Camada de Saída (Densa):
            Número de neurônios: Número de classes
            Função de ativação: Softmax

```
- Complex network
```
      - Camada Convolucional 1: 
            Tamanho da janela: (3, 3)
            Número de filtros: 32
            Função de ativação: ReLU
            Padding: same
      - Camada de Pooling 1 (MaxPooling2D):
            Tamanho da janela: (2, 2)
      - Camada Convolucional 2: 
            Tamanho da janela: (3, 3)
            Número de filtros: 64
            Função de ativação: ReLU
            Padding: same
      - Camada de Pooling 2 (MaxPooling2D):
            Tamanho da janela: (2, 2)
      - Camada Convolucional 3: 
            Tamanho da janela: (3, 3)
            Número de filtros: 128
            Função de ativação: ReLU
            Padding: same
      - Camada de Pooling 3 (MaxPooling2D):
            Tamanho da janela: (2, 2)
      - Camada Convolucional 4: 
            Tamanho da janela: (3, 3)
            Número de filtros: 256
            Função de ativação: ReLU
            Padding: same
      - Camada de Pooling 4 (MaxPooling2D):
            Tamanho da janela: (2, 2)
      - Camada de Achatamento (Flatten):
            Não há parâmetros a serem ajustados.
      - Camada Densa 1 (Fully Connected):
            Número de neurônios: 512
            Função de ativação: ReLU
      - Camada Densa 2 (Fully Connected):
            Número de neurônios: 256
            Função de ativação: ReLU
      - Camada Densa 3 (Fully Connected):
            Número de neurônios: 128
            Função de ativação: ReLU
      - Camada Densa 4 (Fully Connected):
            Número de neurônios: 64
            Função de ativação: ReLU
      - Camada de Saída (Densa):
            Número de neurônios: Número de classes
            Função de ativação: Softmax
```
- Very complex network
```
      - Camada Convolucional 1: 
            Tamanho da janela: (3, 3)
            Número de filtros: 32
            Função de ativação: ReLU
            Padding: same
      - Camada de Pooling 1 (MaxPooling2D):
            Tamanho da janela: (2, 2)
      - Camada Convolucional 2: 
            Tamanho da janela: (3, 3)
            Número de filtros: 64
            Função de ativação: ReLU
            Padding: same
      - Camada de Pooling 2 (MaxPooling2D):
            Tamanho da janela: (2, 2)
      - Camada Convolucional 3: 
            Tamanho da janela: (3, 3)
            Número de filtros: 128
            Função de ativação: ReLU
            Padding: same
      - Camada de Pooling 3 (MaxPooling2D):
            Tamanho da janela: (2, 2)
      - Camada Convolucional 4: 
            Tamanho da janela: (3, 3)
            Número de filtros: 256
            Função de ativação: ReLU
            Padding: same
      - Camada de Pooling 4 (MaxPooling2D):
            Tamanho da janela: (2, 2)
      - Camada de Achatamento (Flatten):
            Não há parâmetros a serem ajustados.
      - Camada Densa 1 (Fully Connected):
            Número de neurônios: 256
            Função de ativação: ReLU
      - Camada de Normalização em Lote (BatchNormalization):
            Aplica normalização em lote para acelerar o treinamento e melhorar o desempenho.
      - Camada Densa 2 (Fully Connected):
            Número de neurônios: 256
            Função de ativação: ReLU
      - Camada de Dropout:
            Taxa de dropout: 0.3
            Ajuda a prevenir overfitting descartando aleatoriamente uma fração dos neurônios durante o treinamento.
      - Camada de Normalização em Lote (BatchNormalization):
            Aplica normalização em lote.
      - Camada de Saída (Densa):
            Número de neurônios: Número de classes
            Função de ativação: Softmax
```


|Dataset        | Melhor Acurácia | Topologia         | Pior Acurácia| Topologia |
| ------------- | -------------   | -------------     | ------------- | ------------- |
|MNIST          |99,30%           |complex_network    |97,84%         |small_network|
|Fashion MNIST  |91,09%           |complex_network    |88,76%         |large_network|
|CIFAR-10       |72.04%           |complex_network    |10%            |small_network |
|CIFAR-100      |29,56%           |large_network      |1%             |small_network|




