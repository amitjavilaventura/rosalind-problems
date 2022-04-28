# ROSALIND PROBLEMS

# Bioinformatics stronghold: https://rosalind.info/problems/list-view/

# Problem 2: Transcribing DNA to RNA -----
# https://rosalind.info/problems/rna/

# We are given a DNA string
# We have to return an RNA string, replacing T for U.
with open("/home/amitjavila/Desktop/Courses/rosalind-problems/stronghold/data_2_transcribe.txt") as f:
    myDNA=f.read()
myRNA = myDNA.replace("T", "U")
print(myRNA)
