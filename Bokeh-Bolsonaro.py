#!/usr/bin/env python
# coding: utf-8

# In[71]:


from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure

output_file("carlos_bolsonaro.html")

##where and how much the brazilian politician, Carlos Bolsonaro is spending his CEAP"
gastos = ['Locação de Veículos', 'Consultorias', 'Manutenção de Escritório', 'Telefonia', 'Outros']
valor = [28563, 21000, 19890, 5255, 6365]

source = ColumnDataSource(data=dict(gastos=gastos, valor=valor, color=Spectral6))

p = figure(x_range=gastos, y_range=(0,50000), plot_height=390, title="Total gasto por Carlos Bolsonaro da Cota Parlamentar em 2020: R$ 81.071,42",
           toolbar_location=None, tools="")

p.vbar(x='gastos', top='valor', width=0.9, color='color', legend_field="gastos", source=source)

p.xgrid.grid_line_color = None
p.legend.orientation = "horizontal"
p.legend.location = "top_center"

show(p)


# In[ ]:




