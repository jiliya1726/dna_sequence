from Bio import SeqIO

# Read the FASTA file 
record = SeqIO.read("sample.fasta", "fasta")

# Convert sequence to upercase
sequence = str(record.seq) .upper()

# Count nucleotide
A = sequence.count("A")
T = sequence.count("T")
G = sequence.count("G")
C = sequence.count("C")                  

# Calculate sequence length
length = len(sequence)

# Calculate GC Content 
gc_content = ((G + C) / length) * 100

# Display result
print("========== DNA Sequence Analysis ==========")
print("Sequence ID :", record.id)
print("Sequence Length :", length)
print(" A :", A)
print(" T :", T)
print(" G :", G)
print(" C :", C)
print("GC Content :", round(gc_content, 2), "%")
