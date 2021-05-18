import streamlit as st
import streamlit.components.v1 as components

features_plot = open('data/features_plot.html', 'r', encoding='utf-8').read()
heat_plot = open('data/heat_plot.html', 'r', encoding='utf-8').read()
histo_plot = open('data/histo_plot.html', 'r', encoding='utf-8').read()
violin_plot = open('data/violin_plot.html', 'r', encoding='utf-8').read()
violin_best_plot = open('data/violin_best_plot.html', 'r', encoding='utf-8').read()

st.write('# Análise de qualidade de vinhos')

st.write('## Histogramas')
components.html(histo_plot, height = 600, width=800)

st.write('## Distribuições de variáveis')
components.html(violin_plot, height = 600, width=800)

st.write('## Correlações entre variáveis')
components.html(heat_plot, height = 600, width=800)

st.write('## Distribuições de variáveis dos melhores vinhos')
components.html(violin_best_plot, height = 600, width=800)

st.write('## Importância das variáveis')
components.html(features_plot, height = 600, width=800)