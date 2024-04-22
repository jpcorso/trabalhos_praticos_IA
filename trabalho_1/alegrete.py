import numpy as np
import sympy as sp


def compute_mse(b, w, data):

    m = len(data)

    quadratic_error = 0.0
    sum = 0.0
    for index, row in enumerate(data):
        x = row[0]
        y = row[1]

        h_theta = b + w*x
        sum += pow((h_theta - y), 2)

    quadratic_error = (1/m)*sum

    # print(quadratic_error)

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

    #quadratic_error_derivative = compute_mse(b, w, data)

    m = len(data)

    sum_b = 0.0
    sum_w = 0.0

    for index, row in enumerate(data):

        x = row[0]
        y = row[1]

        h_theta = b + w*x
        sum_b += 2*(h_theta - y)
        sum_w += 2*x*(h_theta - y)


    b = b - alpha*((1/m)*sum_b)
    w = w - alpha*((1/m)*sum_w)

    # print(b)
    # print(w)
    
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

    list_b = [0]*num_iterations
    list_w = [0]*num_iterations
    
    for i in range(num_iterations):

        b, w = step_gradient(b, w, data, alpha)
        list_b[i] = b
        list_w[i] = w



    # print(list_b)
    # print(list_w)

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


# b = 2
# w = 1
# data = [
#         [11, 2],
#         [14, 4],
#         [2, 4]
#     ]

# alpha = 0.1
# compute = compute_mse(b,w,data)
# gradiente = step_gradient(b, w, data, alpha)

# dataset = np.genfromtxt('alegrete.csv', delimiter=',')

# b_history, w_history = fit(
#     dataset, b=0, w=0,
#     alpha=0.1, num_iterations=100
# )

# print(b_history)
# print(w_history)
