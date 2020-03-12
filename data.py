import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics
import seaborn as sns
import json
from PIL import Image


data = []
sns.set()

###########Get the career groups with more and less initial female inscription in 2007-2019 period################################################
with open("resources/db/grupos.json", "r") as fd:
    for k, v in json.load(fd).items():
        if v[0] == 0:
            data.append([0, k])
            continue
        data.append([v[1] * 100 / v[0], k])

df = pd.DataFrame(data, columns=["percentage", "group"]).sort_values(by="percentage")
print(df)

df.plot(kind="bar", x="group", y="percentage", rot=25, title="Matrícula inicial universitaria por grupos de carreras en el período 2007-2019")
plt.tight_layout()
plt.show()
###################################################################################################################################################

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
