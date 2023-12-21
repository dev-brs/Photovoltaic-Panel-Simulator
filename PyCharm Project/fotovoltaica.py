import numpy as np
import graphics

# Parâmetros fixos
G_ref = 800
k = 1.38e-23
e = 1.60e-19
m = 1.25
Eg = 1.1
Rs = 0.0075
Rp = 1000

# Parâmetros do painel
Voc_ref = 22.65
Isc_ref = 3.8
Vm_ref = 18.53
Im_ref = 3.592
Pm = 66.6
FF = 0.773
Tref = 25
N = 36

# Coeficientes de temperatura
Beta = -82.8e-3
Alpha = 1.15e-2
Gama = -0.4
NOCT = 45
Kt = (45 - 20) / 800

TmodAnterior = 1
TrefK = 273 + Tref

Vtn = N * k * TrefK / e


def exibe(resultado):
    print(f"Potência máxima (W): {resultado}")


def calculo_iv(Tmod, G):
    # Verifica se os parâmetros já existem na lista curvas_iv
    for curva_existente in graphics.curvas_iv:
        if curva_existente['Temp'] == Tmod and curva_existente['Rad'] == G:
            # Parâmetros já existem, saia da função sem calcular
            return curva_existente['Pot_max']

    V = Pmax = I = 0
    curva = {'eixo_x': [], 'eixo_y': [], 'cor_da_curva': [], 'Pot_max': 0, 'Temp': 0, 'Rad': 0, 'Label_X': "",
             'Label_Y': ""}
    TmodK = 273 + Tmod
    IL = (Isc_ref + (Alpha * (Tmod - 25))) * G / 1000
    Voc = Voc_ref + Beta * (Tmod - 25)
    Ion = Isc_ref / (np.exp((Voc / (m * Vtn))) - 1)
    Io = Ion * np.power((TmodK / TrefK), 3) * (np.exp(((e * Eg) / (m * k)) * ((1 / TrefK) - (1 / TmodK))))

    while I >= 0:
        for i in range(10):
            Id = Io * ((np.exp((e / (N * m * k * TmodK)) * (V + Rs * I))) - 1)
            Irp = (V + I * Rs) / Rp
            I = IL - Id - Irp

        pot = V * I
        V = V + 0.1

        if Pmax < pot:
            Pmax = pot
            curva['Pot_max'] = Pmax

        curva['eixo_x'].append(V)
        curva['eixo_y'].append(I)

    curva['cor_da_curva'] = graphics.random_color()
    curva['Temp'] = Tmod
    curva['Rad'] = G
    curva['Label_X'] = "Tensão (V)"
    curva['Label_Y'] = "Corrente (A)"

    graphics.curvas_iv.append(curva)

    return Pmax



def calculo_pot(Tmod, G):
    # Verifica se os parâmetros já existem na lista curvas_pot
    for curva_existente in graphics.curvas_pot:
        if curva_existente['Temp'] == Tmod and curva_existente['Rad'] == G:
            # Parâmetros já existem, saia da função sem calcular
            return curva_existente['Pot_max']

    V = Pmax = I = 0
    curva = {'eixo_x': [], 'eixo_y': [], 'cor_da_curva': [], 'Pot_max': 0, 'Temp': 0, 'Rad': 0, 'Label_X': "",
             'Label_Y': ""}
    TmodK = 273 + Tmod
    IL = (Isc_ref + (Alpha * (Tmod - 25))) * G / 1000
    Voc = Voc_ref + Beta * (Tmod - 25)
    Ion = Isc_ref / (np.exp((Voc / (m * Vtn))) - 1)
    Io = Ion * np.power((TmodK / TrefK), 3) * (np.exp(((e * Eg) / (m * k)) * ((1 / TrefK) - (1 / TmodK))))

    while I >= 0:
        for i in range(10):
            Id = Io * ((np.exp((e / (N * m * k * TmodK)) * (V + Rs * I))) - 1)
            Irp = (V + I * Rs) / Rp
            I = IL - Id - Irp

        pot = V * I
        V = V + 0.1

        if Pmax < pot:
            Pmax = pot
            curva['Pot_max'] = Pmax

        curva['eixo_x'].append(V)
        curva['eixo_y'].append(I * V)

    curva['cor_da_curva'] = graphics.random_color()
    curva['Temp'] = Tmod
    curva['Rad'] = G
    curva['Label_X'] = "Tensão (V)"
    curva['Label_Y'] = "Potência (W)"

    graphics.curvas_pot.append(curva)

    return Pmax


