import plotly.graph_objs as grafico
from plotly.subplots import make_subplots as subplot
import pandas as pd 
import numpy as np


gastos = pd.read_excel("C:\\Users\\Leo\\Desktop\\PythonDashboard\\exemplo.xlsx")

#transforma os nan em float 0.0, retorna uma lista
conversor_para_lista_de_floats =  lambda lst: [float(x) if np.isnan(x) == False else 0 for x in lst] 
entradas_float = conversor_para_lista_de_floats(gastos['Entradas'].values)
saidas_float =  conversor_para_lista_de_floats(gastos['Saídas'].values)
#juntando as entradas e saídas em uma lista só, onde cada elemento é uma lista de 2 posições [entrada,saida]
entradas_e_saidas = list(zip(entradas_float,saidas_float))

#transformando em uma serie pandas indexada pela categoria do gasto
gastos_por_tipo = pd.Series(entradas_e_saidas, index = gastos['Categoria'])

entradas_por_categoria = {}
saidas_por_categoria = {}
ja_foi = []
for categoria in gastos_por_tipo.index.tolist():
    if categoria in ja_foi:
        pass
    else:
        if categoria not in list(entradas_por_categoria.keys()):
            entradas_por_categoria[categoria] = 0
        if categoria not in list(saidas_por_categoria.keys()):
            saidas_por_categoria[categoria] = 0
        for valor in gastos_por_tipo[categoria].values:
            entradas_por_categoria[categoria] += valor[0]
            saidas_por_categoria[categoria]+= valor[1]

x_entradas = list(entradas_por_categoria.keys())
y_entradas = list(entradas_por_categoria.values())

x_saidas = list(saidas_por_categoria.keys())
y_saidas = list(saidas_por_categoria.values())

fig1 = grafico.Figure(data = [grafico.Pie(labels = x_entradas, values = y_entradas)])
fig2 = grafico.Figure(data = [grafico.Pie(labels = x_saidas, values = y_saidas)])

fig1.update_layout(title = 'Entradas')
fig2.update_layout(title = 'Saídas')

fig = subplot(rows = 1, cols = 2, specs=[[{'type':'domain'}, {'type':'domain'}]])
fig.add_trace(fig1.data[0],row = 1, col = 1)
fig.add_trace(fig2.data[0],row = 1, col = 2)
fig.write_html('first_figure.html', auto_open=True)