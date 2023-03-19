import plotly.graph_objs as grafico
from plotly.subplots import make_subplots as subplot
import pandas as pd 
import numpy as np


gastos = pd.read_excel("C:\\Users\\Leo\\Desktop\\PythonDashboard\\exemplo.xlsx")

#transforma os nan em float 0.0, retorna uma lista
conversor_para_lista_de_floats =  lambda lst: [float(x) if np.isnan(x) == False else 0 for x in lst] 
entradas_float = conversor_para_lista_de_floats(gastos['Entradas'].values)
saidas_float =  conversor_para_lista_de_floats(gastos['Saídas'].values)

#transformando em uma serie pandas indexada pela categoria do gasto
entradas_indexadas = pd.Series(entradas_float, index = gastos['Categoria'])
saidas_indexadas = pd.Series(saidas_float, index = gastos['Categoria'])

#agrupando os valores gastos em cada categoria
entradas_agrupadas = entradas_indexadas.groupby('Categoria').sum()
saidas_agrupadas = saidas_indexadas.groupby('Categoria').sum()
print(entradas_agrupadas)
print((entradas_agrupadas != 0))
#tirando os zeros
entradas_agrupadas = entradas_agrupadas.loc[(entradas_agrupadas != 0)]
saidas_agrupadas = saidas_agrupadas.loc[(saidas_agrupadas != 0)]

labels_entradas = entradas_agrupadas.index.tolist()
labels_saidas = saidas_agrupadas.index.tolist()
valores_entradas = entradas_agrupadas.values.tolist()
valores_saidas = saidas_agrupadas.values.tolist()

fig1 = grafico.Figure(data = [grafico.Pie(labels = labels_entradas, values = valores_entradas)])
fig2 = grafico.Figure(data = [grafico.Pie(labels = labels_saidas, values = valores_saidas)])

fig1.update_layout(title = 'Entradas')
fig2.update_layout(title = 'Saídas')

fig = subplot(rows = 1, cols = 2, specs=[[{'type':'domain'}, {'type':'domain'}]])
fig.add_trace(fig1.data[0],row = 1, col = 1)
fig.add_trace(fig2.data[0],row = 1, col = 2)
fig.write_html('first_figure.html', auto_open=True)