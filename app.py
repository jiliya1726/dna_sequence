import io

import streamlit as st 
from Bio import SeqIO

st.title("DNA Sequence Analysis")

# 1. File Uploader
text_file = st.file_uploader("Upload FASTA File", type=["fasta", "fa"])

if text_file is not None:
# 1. Read all records using parse
    stringio =  io.StringIO(text_file.getvalue().decode("utf-8"))
    records = list(SeqIO.parse(stringio,"fasta"))

    st.write("**Number of sequence:**", len(records))

    # 2. Loop through each record (Minimal Change)
    for record in records:
        sequence = str(record.seq) .upper()
A = sequence.count("A")
T = sequence.count("T")
G = sequence.count("G")
C = sequence.count("C") 
length = len(sequence)
gc_content =((G + C) / length )* 100

st.subheader("Analysis Result")
st.write("**Sequence ID:**", record.id)
st.write("**Sequence Length:**", length)

st.write("### Nucleotide Count")
st.write("A :", A)
st.write("T :", T)
st.write("G :", G)
st.write("C :", C)

st.write("### GC Content")

st.success(f"{gc_content:.2f}%")
