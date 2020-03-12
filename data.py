import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics
import seaborn as sns
import json
from PIL import Image


def percentage(p, t):
    return p * 100 / t

data = []
sns.set()

###########Get the career groups with more and less initial female inscription in 2012-2018 period################################################
# with open("resources/db/grupos.json", "r") as fd:
#     for k, v in json.load(fd).items():
#         if v[0] == 0:
#             data.append([0, k])
#             continue
#         data.append([v[1] * 100 / v[0], k])

# df = pd.DataFrame(data, columns=["porciento", "grupos"]).sort_values(by="porciento")
# print(df)

# df.plot(kind="bar", x="grupos", y="porciento", rot=25, title="Matrícula inicial universitaria por grupos de carreras en el curso 2017-2018")
# plt.tight_layout()
# plt.show()
###################################################################################################################################################

########Compare the total of graduates of men with women, for career groups. Get the groups with more and less female graduates 2006-2018####################
data.clear()
female = []
periods = ["2006/07", "2007/08", "2008/09", "2009/10", "2010/11", "2011/12", "2012/13", "2013/14", "2014/15", "2015/16", "2016/17", "2017/18"]

with open("resources/db/graduaciones.json", "r") as fd:
    data = json.load(fd)
    dfTotal = pd.DataFrame(data, index=periods)
    dfPer = pd.DataFrame(data, index=periods)

with open("resources/db/graduaciones(mujeres).json", "r") as fd:
    data = json.load(fd)
    dfF = pd.DataFrame(data, index=periods)

for p in periods:
    for i in range(len(dfTotal.loc[p])):
        dfPer.loc[p][i] = dfF.loc[p][i] * 100 / dfTotal.loc[p][i]

print(dfPer)
# tight_layout manually
dfPer.plot(title="Porcentaje de graduados(mujeres) por curso")
plt.xticks(range(len(dfPer.index)), dfPer.index)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

# mean of groups across period
PerM = dfPer.mean(0)

# Best mean for female
BestM = [[g, p] for g, p in PerM.items() if p >= 50]
dfBestM = pd.DataFrame(BestM, columns=["grupos", "porciento"]).sort_values(by="porciento")
print(dfBestM)

dfBestM.plot(kind="bar", x="grupos", y="porciento", rot=25, title="Grupos de carreras con mayor media de porcentajes de graduados(mujeres) en el período 2006-2018")
plt.tight_layout()
#plt.show()

# Best mean for male
BestM = [[g, 100 - p] for g, p in PerM.items() if p <= 50]
dfBestM = pd.DataFrame(BestM, columns=["grupos", "porciento"]).sort_values(by="porciento")
print(dfBestM)

dfBestM.plot(kind="bar", x="grupos", y="porciento", rot=25, title="Grupos de carreras con mayor media de porcentajes de graduados(hombres) en el período 2006-2018")
plt.tight_layout()
plt.show()

####################################################################################################################################################
text1 = '''
Hay carreras universitarias en nuestro país cuya matrícula es predominantemente femenina. No es un fenómeno particular de una 
institución, sino es un hecho común en todas las universidades del país. Puede se de interés cuáles son 
las carreras con mayor aglomeración de mujeres y qué tienen estas en común que les resultan tan atractivas o viceversa.
'''

#Á É Í Ó Ú á é í ó ú ñ


# def plot_bar_x():
#     index = np.arange(len(labels))
#     plt.bar(index, values)
#     plt.xlabel("Grupos de Carreras", fontsize=10)
#     plt.ylabel("Cantidad de Mujeres", fontsize=10)
#     plt.xticks(index, labels, fontsize=5, rotation=25)
#     plt.title("Cantidad de mujeres por grupo de carreras universitarias")
#     plt.show()

#image = Image.open("Figure_2.jpeg")
#st.image(image)#, width=2000)

# # with open("Figure_1.png", "r") as img:
# #     st.image(img)
