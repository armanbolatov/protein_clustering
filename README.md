# Protein Ligand Interaction Visualizer

This application provides a 3D visualization of protein-ligand interactions based on various parameters (`pKi`, `pKd`, `pIC50`, `pEC50`). 

The visualizations are based on protein embeddings obtained from a pre-trained model, specifically [ProtBERT](https://huggingface.co/Rostlab/prot_bert). The embeddings are reduced to three dimensions using [UMAP](https://umap-learn.readthedocs.io/en/latest/).

The application allows you to select a specific ligand and a parameter of interest from the dropdown menus. The corresponding 3D scatter plot generated using Plotly is then displayed, with each point representing a protein. The color of the points indicates the value of the selected parameter for the interaction between the protein and the ligand.

![image](https://github.com/user-attachments/assets/33f439cd-09a7-4162-9f7f-18ca9bf92bc5)
