import numpy as np
import sympy as sp


def compute_mse(b, w, data):

    data = [
        [11, 2],
        [14, 4],
        [2, 4]
    ]
    m = len(data)

    quadratic_error = 0.0
    sum = 0.0
    for index, row in enumerate(data):
        x = row[0]
        y = row[1]

        h_theta = b + w*x
        sum += pow((h_theta - y), 2)

    quadratic_error = (1/m)*sum

    """
    Calcula o erro quadratico medio
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """
    return quadratic_error

    #raise NotImplementedError  # substituir pelo seu codigo


def step_gradient(b, w, data, alpha):

    quadratic_error_derivative = compute_mse(b, w, data)

    #b = b - alpha*quadratic_error
    #w = w - alpha*quadratic_error
    
    return b, w
    """
    Executa uma atualização por descida do gradiente  e retorna os valores atualizados de b e w.
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de b e w, respectivamente
    """
    raise NotImplementedError  # substituir pelo seu codigo


def fit(data, b, w, alpha, num_iterations):
    list_b = []
    list_w = []
    for i in range(num_iterations):

        gradient = step_gradient(b, w, data, alpha)

    
    return list_b, list_w

    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de b e w.
    Ao final, retorna duas listas, uma com os b e outra com os w
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os b e outra com os w obtidos ao longo da execução
    """

    raise NotImplementedError  # substituir pelo seu codigo

#compute_mse(0,0,0)
