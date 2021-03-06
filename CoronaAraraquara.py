#!/usr/bin/env python
# coding: utf-8

# In[58]:


## This is a simple graph about the coronavirus situaiton in my home town, Araraquara.

## Matplotlib and NumPy
import matplotlib.pyplot as plt
import numpy as np

plt.rcdefaults()
fig, ax = plt.subplots()

## infectados = Infected, in quarantine, recovered, suspected deaths, confirmed deaths
## casos = numbers of the respective "infectados"
infectados = ('Infectados', 'Recuperados', 'Em Quarentena', 'Mortes Suspeitas', 'Mortes')
y_pos = np.arange(len(infectados))
casos = [147, 121, 22, 4, 4]

for i, v in enumerate(casos):
    ax.text(v + 1, i + .1, str(v), color='black')

ax.barh(y_pos, casos, xerr=error, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(infectados)
ax.invert_yaxis()
ax.set_xlabel('Casos')
ax.set_title('Coronavírus em Araraquara - 18 de Maio de 2020')

plt.show()


# In[ ]:




