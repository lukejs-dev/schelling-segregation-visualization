import streamlit as st
import random
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

import src.classes as classes

st.title("Schelling's Segregation Model")

population_size = st.sidebar.slider("Population Size", 500, 10000, 2500)
empty_ratio = st.sidebar.slider("Empty Houses Ratio", 0., 1., .2)
similarity_threshold = st.sidebar.slider("Similarity Threshold", 0., 1., .4)
n_iterations = st.sidebar.number_input("Number of Iterations", 50)

schelling = classes.Schelling(population_size, empty_ratio, similarity_threshold, 3)
mean_similarity_ratio = []
mean_similarity_ratio.append(schelling.get_mean_similarity_ratio())

plt.style.use("ggplot")
plt.figure(figsize=(8, 4))

cmap = ListedColormap(['red', 'white', 'royalblue'])
plt.subplot(121)
plt.axis('off')
plt.pcolor(schelling.city, cmap=cmap, edgecolors='w', linewidths=1)

plt.subplot(122)
plt.xlabel("Iterations")
plt.xlim([0, n_iterations])
plt.ylim([0.4, 1])
plt.title("Mean Similarity Ratio", fontsize=15)
plt.text(1, 0.95, "Similarity Ratio: %.4f" % schelling.get_mean_similarity_ratio(), fontsize=10)

city_plot = st.pyplot(plt)

progress_bar = st.progress(0)

if st.sidebar.button("Run Simulation"):

    for i in range(n_iterations):
        schelling.run()
        mean_similarity_ratio.append(schelling.get_mean_similarity_ratio())
        plt.figure(figsize=(8, 4))

        plt.subplot(121)
        plt.axis('off')
        plt.pcolor(schelling.city, cmap=cmap, edgecolors='w', linewidths=1)

        plt.subplot(122)
        plt.xlabel("Iterations")
        plt.xlim([0, n_iterations])
        plt.ylim([0.4, 1])
        plt.title("Mean Similarity Ratio", fontsize=15)
        plt.plot(range(1, len(mean_similarity_ratio)+1), mean_similarity_ratio)
        plt.text(1, 0.95, "Similarity Ratio: %.4f" % schelling.get_mean_similarity_ratio(), fontsize=10)

        city_plot.pyplot(plt)
        plt.close("all")
        progress_bar.progress((i+1.)/n_iterations)