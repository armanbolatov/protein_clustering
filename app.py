import os
import streamlit as st
import plotly.graph_objects as go
import json

PATH = "plots/"

st.set_page_config(
    page_title="Protein-Ligand Interaction Visualizer",
    page_icon="🧬",
    initial_sidebar_state="expanded",
)
st.title("Protein-Ligand Interaction Visualizer 🧬")
st.markdown("""
Welcome to the Protein-Ligand Interaction Visualizer. This application provides a 3D visualization of protein-ligand interactions based on various parameters (`pKi`, `pKd`, `pIC50`, `pEC50`). 

The visualizations are based on protein embeddings obtained from a pre-trained model, specifically [ProtBERT](https://huggingface.co/Rostlab/prot_bert). The embeddings are reduced to three dimensions using [UMAP](https://umap-learn.readthedocs.io/en/latest/).

The application allows you to select a specific ligand and a parameter of interest from the dropdown menus. The corresponding 3D scatter plot generated using Plotly is then displayed, with each point representing a protein. The color of the points indicates the value of the selected parameter for the interaction between the protein and the ligand.

The data used in this application comes from [BindingDB](https://www.bindingdb.org/bind/index.jsp).
""")

parameter = st.selectbox("Parameter", os.listdir(PATH))

ligand_names = os.listdir(os.path.join(PATH, parameter))
ligand_names = [ligand_name.split(".")[0] for ligand_name in ligand_names]

ligand = st.selectbox("Ligand", ligand_names)

path_to_json = os.path.join(PATH, parameter, ligand + ".json")

with st.spinner("Loading plot..."):
    with open(path_to_json, 'r') as json_file:
        fig_json = json_file.read()
    fig = go.Figure(json.loads(fig_json))
    st.plotly_chart(fig)