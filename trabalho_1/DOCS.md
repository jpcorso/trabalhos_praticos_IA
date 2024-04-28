## Como configurar o ambiente?
O Google Collab já é um ambiente configurado.
Pra rodar localmente, usar ```venv```

## Bibliotecas utilizadas
#### Tensorflow 
Biblioteca de código aberto para aprendizado de máquina e inteligência artificial. 
Serve para:
- Construir e treinar modelos de aprendizagem de máquina
- Executar modelos em diferentes ambientes (CPUs, GPUs, TPUs)
- Criar aplicações de inteligência artificial

#### Keras
Biblioteca construida sobre o **TensorFlow**

>Simplifica a interação com o TensorFlow, permitindo que usuários com diferentes níveis de conhecimento técnico possam criar e treinar modelos de forma eficiente.

### Datasets

```keras.datasets``` é um modulo que fornece acesso a conjuntos de dados pré-processados para serem utilizados em machine learning e deep learning. 

A importação de conjuntos de dados pré-prontos no TensorFlow pode ser utilizada tanto para aprendizagem quanto para aplicação de machine learning.

#### Funções dentro do módulo ```keras.datasets```
Essas funções retornam duas tuplas de NumPy arrays:
- **(x_train, y_train)**: Contém as imagens de treinamento e seus rótulos (classes).
- **(x_test, y_test)**: Contém as imagens de teste e seus rótulos (classes).

**train_labels (y_train)**, **test_labels (y_test)** são rótulos escalares que posteriormente são convertidos para *one-hot encoding*.   



```keras.datasets.cifar10``` carrega o conjunto de dados CIFAR-10 

>CIFAR-10 é um conjunto de imagens de objetos do dia a dia, como carros, aviões, animais e outros.


```keras.datasets.cifar100``` carrega o conjunto de dados CIFAR-100

>CIFAR-100 Contém imagens coloridas (32x32 pixels) de 100 classes diferentes de objetos do cotidiano, agrupadas em 20 categorias superiores (animais, meios de transporte, etc.)


```keras.datasets.mnist```carrega o conjunto de dados MNIST
>MNIST é composto por imagens (64x64 pixels) de dígitos manuscritos (de 0 a 9) e seus rótulos correspondentes.


```keras.datasets.fashionmnist``` carrega o conjunto de dados Fashion-MNIST 
>Fashion-MNIST é uma alternativa ao MNIST e contém imagens (28x28 pixels) de 10 categorias de roupas e acessórios (camiseta, calça, casaco, etc.) e seus rótulos.





### Rede Neural Convolucional
>Redes neurais convolucionais (ConvNets ou CNNs) são utilizadas com mais frequência para tarefas de classificação e visão computacional. Antes das CNNs, métodos de extração de recursos manuais e demorados eram usados para identificar objetos em imagens. No entanto, as redes neurais convolucionais agora oferecem uma abordagem mais dimensionável para tarefas de classificação de imagens e reconhecimento de objetos, aproveitando os princípios da álgebra linear, especificamente a multiplicação de matrizes, para identificar padrões em uma imagem. Dito isso, elas podem exigir muito da computação, o que exige unidades de processamento gráfico (GPUs) para treinar modelos.


#### Filtros e features maps
Algumas camadas contém unidades de processamento
especializadas chamadas de filtros (kernels).
- Filtros realizam operações de convolução (uma multiplicação elemento a elemento entre o filtro e uma parte da imagem de
entrada, delimitada por uma janela que se move ao longo da imagem)
    - Deslocando a janela e aplicando o filtro a todas as partes da imagem, geramos um mapa de características (*feature map*), que indica onde e com que intensidade a característica representada
pelo filtro é detectada na imagem.
- Detectam a presença e localização de certas características
relevantes para a tarefa.
- São aprendidos automaticamente a partir dos dados.



#### Max Pooling
- Reduz a resolução e tamanho dos feature maps gerados pelas camadas
convolucionais.

    - Seleciona-se uma janela (como 2X2, 3X3,...)
    - Seleciona-se um passo de deslocamento (stride, como 2)
    - A janela é movida ao longo de um feature map considerando o stride
    - Para cada janela, é selecionado o maior valor, para compor uma versão
    reduzida do feature map


#### Hiperparâmetros 
Parâmetros configurados pelo projetista. 

- **Arquitetura**: quais e quantas camadas, de que tipo e em que sequência estão organizadas

    <span style="color:cyan"> 
    A quantidade de níveis está relacionada a <b>complexidade das características</b> (níveis mais profundos para características mais abstratas) 
    </span>
    <br><br>

- **Número de filtros, tamanho dos filtros, stride da janela** nas camadas convolucionais

    <span style="color:cyan"> 
    O número de filtros está associado ao <b>número de características</b> diferentes identificadas em cada nível.<br> É comum começar com menos e aumentar ao longo da rede. 
    </span>
    <br><br>

    <span style="color:cyan"> 
    O tamanho do filtro está associado à <b>escala</b> em que a feature é detectada. <br> É comum começar com tamanhos menores e aumentar o tamanho ao longo da rede. 
    </span>
    <br><br>

- **Tamanho da janela e stride** nas camadas de pooling

    <span style="color:cyan"> 
    Mais operações de max pooling aumentam <b>tolerância a translações</b>
    </span>
    <br><br>


- **Número de neurônios e de camadas** na MLP (Perceptron Multicamadas) usada no fim da rede
    
    <span style="color:cyan"> 
    Mais neurônios e camadas aumentam a <b>complexidade do modelo</b> e o risco de overfiting. <br> Entretanto, <b>mais dados de treinamento</b> permitem redes mais complexas e diminuem o risco de overfitting. 
    </span>
    <br><br>



### Funções 
**```model = keras.Sequential()```** define um modelo sequencial do Keras. Um modelo sequencial empilha camadas de rede neural uma após a outra, onde a saída de uma camada se torna a entrada da próxima camada.

```
model = keras.Sequential([
      tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
      tf.keras.layers.MaxPooling2D((2, 2)),
      tf.keras.layers.Conv2D(128, (3, 3), activation='relu', input_shape=(28, 28, 1)),  
      tf.keras.layers.MaxPooling2D((2, 2)),
      tf.keras.layers.Flatten(),
      tf.keras.layers.Dense(64, activation='relu'),
      tf.keras.layers.Dense(num_classes, activation='softmax') 
  ])
  ```




**```Conv2D```** definem as camadas convolucionais 2D, onde se aplicam os filtros para adquirir características visuais
```
keras.layers.Conv2D(
    filters,
    kernel_size,
    strides=(1, 1),
    padding="valid",
    data_format=None,
    dilation_rate=(1, 1),
    groups=1,
    activation=None,
    use_bias=True,
    kernel_initializer="glorot_uniform",
    bias_initializer="zeros",
    kernel_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    bias_constraint=None,
    **kwargs
)
```



**```MaxPooling2D```** definem as camadas de pooling 2D
```
keras.layers.MaxPooling2D(
    pool_size=(2, 2), strides=None, padding="valid", data_format=None, name=None, **kwargs
)
```


**```Flatten```** define a camada flatten, que converte a representação tridimensional da saída das camadas convolucionais em uma representação unidimensional
```
keras.layers.Flatten(data_format=None, **kwargs)
```


**```Dense```** definem as camadas totalmente conectadas, que funcionam com os neurônios clássicos
```
keras.layers.Dense(
    units,
    activation=None,
    use_bias=True,
    kernel_initializer="glorot_uniform",
    bias_initializer="zeros",
    kernel_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    bias_constraint=None,
    lora_rank=None,
    **kwargs
)
```

**```model.compile()```** Prepara o modelo para treinamento, definindo o otimizador, a função de perda e as métricas de avaliação.
```
compile(
    optimizer='rmsprop',
    loss=None,
    loss_weights=None,
    metrics=None,
    weighted_metrics=None,
    run_eagerly=False,
    steps_per_execution=1,
    jit_compile='auto',
    auto_scale_loss=True
)
```

**```model.summary()```** Fornece uma visão geral da arquitetura e da configuração do modelo, facilitando a compreensão e a depuração.

**```model.fit()```** Treina modelo para um número fixo de épocas.
```
fit(
    x=None,
    y=None,
    batch_size=None,
    epochs=1,
    verbose='auto',
    callbacks=None,
    validation_split=0.0,
    validation_data=None,
    shuffle=True,
    class_weight=None,
    sample_weight=None,
    initial_epoch=0,
    steps_per_epoch=None,
    validation_steps=None,
    validation_batch_size=None,
    validation_freq=1
)
```


**```model.evaluate()```** Retorna o valor da perda e os valores das métricas para o modelo em modo de teste.

```
evaluate(
    x=None,
    y=None,
    batch_size=None,
    verbose='auto',
    sample_weight=None,
    steps=None,
    callbacks=None,
    return_dict=False,
    **kwargs
)
```




--- 
Baseado na [documentação do TensorFLow](https://www.tensorflow.org/?hl=pt-br), no [site da IBM](https://www.ibm.com/br-pt/topics/convolutional-neural-networks), nos slides da disciplina e feito com o auxilio do [Gemini](https://gemini.google.com/app/). 
