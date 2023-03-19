import plotly.graph_objs as grafico
from plotly.subplots import make_subplots as subplot
import openpyxl

gastos = openpyxl.load_workbook("C:\\Users\\Leo\\Desktop\\PythonDashboard\\exemplo.xlsx", data_only=True)

gastos = gastos.active

lista_de_categorias= list([cell.value for cell in gastos['E']])
lista_de_saidas = list([cell.value for cell in gastos['H']])
lista_de_entradas = list([cell.value for cell in gastos['G']])

concatenados = [(x,y,z) for x,y,z in zip(lista_de_categorias,lista_de_saidas,lista_de_entradas)]

gastos_por_tipo ={}
for transacao in concatenados:
    tipo, entrada, saida = transacao
    tipo = tipo if tipo is not None else "Desconhecido"
    entrada = entrada if entrada is not None else 0
    saida = saida if saida is not None else 0
    if tipo not in gastos_por_tipo:
        gastos_por_tipo[tipo] = [entrada,saida]
    else:
        gastos_por_tipo[tipo][0] += entrada
        gastos_por_tipo[tipo][1] += saida

entradas = {}
saidas = {}

for key in gastos_por_tipo.keys():
    if gastos_por_tipo[key][0] != 0:
        entradas[key] = gastos_por_tipo[key][0]
    if gastos_por_tipo[key][1] != 0:
        saidas[key] = gastos_por_tipo[key][1]

x_entradas = list(entradas.keys())
y_entradas = list(entradas.values())

x_saidas = list(saidas.keys())
y_saidas = list(saidas.values())

fig1 = grafico.Figure(data = [grafico.Pie(labels = x_entradas, values = y_entradas)])
fig2 = grafico.Figure(data = [grafico.Pie(labels = x_saidas, values = y_saidas)])
fig1.update_layout(title = 'Entradas')
fig2.update_layout(title = 'Saídas')

fig = subplot(rows = 1, cols = 2, specs=[[{'type':'domain'}, {'type':'domain'}]])
fig.add_trace(fig1.data[0],row = 1, col = 1)
fig.add_trace(fig2.data[0],row = 1, col = 2)
fig.write_html('first_figure.html', auto_open=True)