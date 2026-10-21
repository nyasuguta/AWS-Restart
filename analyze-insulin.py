
from pathlib import Path
import re

# Change this to match the name of your original sequence file
input_file = Path("preproinsulin-seq.txt")

# Read the original sequence
raw = input_file.read_text()

# Extract the sequence after ORIGIN and remove numbering,
# spaces, line breaks, and the // terminator.
sequence = raw.split("ORIGIN", 1)[-1]
sequence = sequence.split("//", 1)[0]
sequence = re.sub(r"[^a-zA-Z]", "", sequence).lower()

# Verify the complete preproinsulin sequence
assert len(sequence) == 110, (
    f"Expected 110 amino acids, found {len(sequence)}"
)

# Save the complete cleaned sequence
Path("preproinsulin-seq-clean.txt").write_text(sequence)

# Split the sequence using Python's zero-based indexing
sections = {
    "lsinsulin-seq-clean.txt": sequence[0:24],
    "binsulin-seq-clean.txt": sequence[24:54],
    "cinsulin-seq-clean.txt": sequence[54:89],
    "ainsulin-seq-clean.txt": sequence[89:110],
}

# Save each section and verify its length
for filename, fragment in sections.items():
    Path(filename).write_text(fragment)
    print(f"{filename}: {len(fragment)} characters")

print(f"preproinsulin-seq-clean.txt: {len(sequence)} characters")
print("All files created successfully.")


insulin = binsulin + ainsulin 
# Calculating the molecular weight of insulin  
# Creating a list of the amino acid (AA) weights  
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}  
# Count the number of each amino acids  
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']})  
# Multiply the count by the weights  
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values())  
print("The rough molecular weight of insulin: " +
str(molecularWeightInsulin))