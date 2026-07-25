import streamlit as st
from Bio import SeqIO

st.title("Analysis")

# 1. Show the upload button
uploaded_file = st.file_uploader("Upload FASTA File", type=["fasta", "fa"])

# 2. ONLY run the sequence logic IF a file has actually been uploaded
if uploaded_file is not None:
    # Decode the uploaded file
    stringio = uploaded_file.getvalue().decode("utf-8")
    
    # Read the sequence from the FASTA file
    for record in SeqIO.parse(uploaded_file, "fasta"):
        sequence = str(record.seq)  # <--- Creates the 'sequence' variable
        
        # Now count the letters safely
        A = sequence.count("A")
        st.write(f"A count: {A}")
