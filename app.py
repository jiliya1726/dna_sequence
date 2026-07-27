import io
import matplotlib.pyplot as plt
import streamlit as st
from Bio import SeqIO

# Page Configuration
st.set_page_config(page_title="DNA Sequence Analysis", layout="centered")

st.title("🧬 DNA Sequence Analysis App")
st.write(
    "Upload a FASTA file below to analyze nucleotide frequencies and sequence metrics."
)

# File Uploader
uploaded_file = st.file_uploader("Upload FASTA File", type=["fasta", "fa"])

if uploaded_file is not None:
  # Decode binary file stream into text stream
  stringio = io.StringIO(uploaded_file.getvalue().decode("latin-1"))

  # Iterate through records in the FASTA file
  for record in SeqIO.parse(stringio, "fasta"):
    st.subheader(f"Sequence Header: {record.id}")

    sequence = str(record.seq).upper()
    seq_length = len(sequence)

    # Calculate Nucleotide Counts
    counts = {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "C": sequence.count("C"),
        "G": sequence.count("G"),
    }

    # Calculate GC Content Percentage
    gc_content = (
        ((counts["G"] + counts["C"]) / seq_length * 100) if seq_length > 0 else 0
    )

    # Display Metrics in Columns
    col1, col2, col3 = st.columns(3)
    col1.metric("Sequence Length", f"{seq_length:,} bp")
    col2.metric("GC Content", f"{gc_content:.2f}%")
    col3.metric("AT Content", f"{100 - gc_content:.2f}%")

    st.markdown("---")

    # Display Base Counts
    st.subheader("📊 Base Counts")
    st.write(
        f"**Adenine (A):** {counts['A']:,} | "
        f"**Thymine (T):** {counts['T']:,} | "
        f"**Cytosine (C):** {counts['C']:,} | "
        f"**Guanine (G):** {counts['G']:,}"
    )

    # Graph 1: Bar Chart (Nucleotide Frequency)
    st.subheader("📈 Nucleotide Frequency (Bar Chart)")
    fig1, ax1 = plt.subplots(figsize=(7, 4))
    colors = ["#4C72B0", "#DD8452", "#55A868", "#C44E52"]
    ax1.bar(counts.keys(), counts.values(), color=colors)
    ax1.set_xlabel("Bases")
    ax1.set_ylabel("Count")
    ax1.set_title("Nucleotide Frequency Distribution")
    st.pyplot(fig1)

    # Graph 2: Pie Chart (Base Composition)
    st.subheader("🥧 Base Composition (Pie Chart)")
    fig2, ax2 = plt.subplots(figsize=(6, 6))
    ax2.pie(
        counts.values(),
        labels=counts.keys(),
        autopct="%1.1f%%",
        startangle=140,
        colors=colors,
    )
    ax2.set_title("Nucleotide Composition Ratio")
    st.pyplot(fig2)

else:
  st.info("Please upload a `.fasta` or `.fa` file to begin analysis.")
