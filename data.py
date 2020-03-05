import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
from PIL import Image

labels = []
values = []
with open("grupos.json", "r") as fd:
    for k, v in json.load(fd).items():
        labels.append(k)
        values.append(v[1] * 100 / v[0])

# print(labels)
# print(values)

st.title("Mujeres en la universidad")

text1 = '''
Hay carreras universitarias en nuestro país cuya matrícula es predominantemente femenina. No es un fenómeno particular de una 
institución, sino es un hecho común en todas las universidades del país. Puede se de interés cuáles son 
las carreras con mayor aglomeración de mujeres y qué tienen estas en común que les resultan tan atractivas o viceversa.
'''

st.write(text1)

def plot_bar_x():
    index = np.arange(len(labels))
    plt.bar(index, values)
    plt.xlabel("Grupos de Carreras", fontsize=10)
    plt.ylabel("Cantidad de Mujeres", fontsize=10)
    plt.xticks(index, labels, fontsize=5, rotation=25)
    plt.title("Cantidad de mujeres por grupo de carreras universitarias")
    #plt.show()

plot_bar_x()
st.pyplot()

#image = Image.open("Figure_2.jpeg")
#st.image(image)#, width=2000)

# # with open("Figure_1.png", "r") as img:
# #     st.image(img)
