import matplotlib.pyplot as plt
import random
import numpy as np

curvas_iv = []
curvas_pot = []


def reset_graphics():
    print("Resetando gráficos")
    curvas_iv.clear()
    curvas_pot.clear()


def random_color():
    # Gerar três valores aleatórios entre 0 e 255
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)

    # Retornar uma lista com os valores
    return [R, G, B]


def plot_pot(todas_as_curvas):
    print("Plotando gráfico potência")
    plt.ion()
    for curva in todas_as_curvas:
        eixo_x = curva["eixo_x"]
        eixo_y = curva["eixo_y"]
        cor_da_curva = curva["cor_da_curva"]
        temperatura = curva["Temp"]
        radiacao = curva["Rad"]

        label = f"Curva {temperatura}°C - {radiacao}W/m²"

        plt.plot(eixo_x, eixo_y, label=label,
                 color=(cor_da_curva[0] / 255, cor_da_curva[1] / 255, cor_da_curva[2] / 255))

    plt.xlabel('Tensão (V)')
    plt.ylabel('Potência (W)')
    plt.title('Curvas Características do Painel Solar')
    plt.legend()

    plt.grid(True)
    plt.show()
    plt.pause(6)
    plt.close()


def plot_iv(todas_as_curvas):
    print("Plotando gráfico IV")
    plt.ion()
    for curva in todas_as_curvas:
        eixo_x = curva["eixo_x"]
        eixo_y = curva["eixo_y"]
        cor_da_curva = curva["cor_da_curva"]
        temperatura = curva["Temp"]
        radiacao = curva["Rad"]

        label = f"Curva {temperatura}°C - {radiacao}W/m²"

        plt.plot(eixo_x, eixo_y, label=label,
                 color=(cor_da_curva[0] / 255, cor_da_curva[1] / 255, cor_da_curva[2] / 255))

    plt.xlabel('Tensão (V)')
    plt.ylabel('Corrente (W)')
    plt.title('Curvas Características do Painel Solar')
    plt.legend()
    plt.grid(True)
    plt.show()
    plt.pause(6)
    plt.close()


def fechar_graficos():
    plt.close('all')
