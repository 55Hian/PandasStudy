# -*- coding: utf-8 -*-
"""main.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hBaRHpzNEgGIzMIFDNbW8PaAHQ-VzJhR

André Luiz Veras Fernades
"""

import pandas as pd

"""a)"""

dados =  pd.read_excel("Base Funcionarios.xlsx")
print(dados)

dados =  pd.read_excel("Base Funcionarios.xlsx")
Res = list(dados["Sexo"] == "F")
print(dados.loc[Res])

"""b)"""

ModificarF = list(dados["Sexo"] == "F")
ModificarM = list(dados["Sexo"] == "M")

dados.at[ModificarF,"Sexo"] = "Feminino"
dados.at[ModificarM,"Sexo"] = "Masculino"

dados

"""c)"""

Res = list(dados["Setor"] == "Recursos Humanos")
print(dados.loc[Res])

"""d)"""



"""e)"""

SomaRendaV = list(dados["Setor"] == "Mesa de Renda Variável")

print(dados.Salário.sum())
print(dados.loc[SomaRendaV].Salário.sum())

"""Bonus"""

