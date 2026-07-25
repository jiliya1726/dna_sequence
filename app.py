import io
import matplotlib.pyplot as plt
import streamlit as st
from Bio import SeqIO

st.title("DNA Sequence Analysis")

uploaded_file = st.file_uploader("Upload FASTA File", type=["fasta", "fa"])

if uploaded_file is not None:
  # Convert binary uploaded file to a text stream
  stringio = io.StringIO(uploaded_file.getvalue().decode("utf-8"))

  for record in SeqIO.parse(stringio, "fasta"):
    sequence = str(record.seq).upper()

    # Calculate base counts
    counts = {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "C": sequence.count("C"),
        "G": sequence.count("G"),
    }

    # Display text counts
    st.write(
        f"**A:** {counts['A']} | **T:** {counts['T']} | **C:** {counts['C']} |"
        f" **G:** {counts['G']}"
    )

    # Plot the chart
    fig, ax = plt.subplots()
    ax.bar(
        counts.keys(), counts.values(), color=["blue", "red", "green", "orange"]
    )
    ax.set_ylabel("Count")
    ax.set_title("Nucleotide Frequency")

    # Display plot in Streamlit
    st.pyplot(fig)
