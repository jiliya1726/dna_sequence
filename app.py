import streamlit as st
from Bio import SeqIO
import matplotlib.pyplot as plt

st.title("DNA Sequence Analysis")

uploaded_file = st.file_uploader("Upload FASTA File", type=["fasta", "fa"])

if uploaded_file is not None:
    for record in SeqIO.parse(uploaded_file, "fasta"):
        sequence = str(record.seq).upper()
        
        # Calculate counts
        counts = {
            'A': sequence.count('A'),
            'T': sequence.count('T'),
            'C': sequence.count('C'),
            'G': sequence.count('G')
        }
        
        # Create plot figure
        fig, ax = plt.subplots()
        ax.bar(counts.keys(), counts.values(), color=['blue', 'red', 'green', 'orange'])
        ax.set_ylabel("Count")
        ax.set_title("Nucleotide Frequency")
        
        # Display the graph on screen
        st.pyplot(fig)

