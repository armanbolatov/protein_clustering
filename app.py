import os
import streamlit as st
import plotly.graph_objects as go
import json

PATH = "plots/"

parameter = st.selectbox(
    "Parameters",
    os.listdir(PATH)
)

ligand_names = os.listdir(os.path.join(PATH, parameter))
ligand_names = [ligand_name.split(".")[0] for ligand_name in ligand_names]

ligand = st.selectbox(
    "Ligand",
    ligand_names
)

path_to_json = os.path.join(PATH, parameter, ligand + ".json")

with st.spinner("Loading plot..."):
    with open(path_to_json, 'r') as json_file:
        fig_json = json_file.read()
    fig = go.Figure(json.loads(fig_json))
    st.plotly_chart(fig)