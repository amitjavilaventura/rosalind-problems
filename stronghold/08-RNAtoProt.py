# ROSALIND PROBLEMS

# Bioinformatics stronghold: https://rosalind.info/problems/list-view/

# Problem 8: Translate RNA to protein -----
# https://rosalind.info/problems/iprb/

# We are given a RNA string
# We have to return the protein sequence in one letter code.

# === Define RNA codons 
RNA_Codons = {
    # 'M' - START, '_' - STOP
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UGU": "C", "UGC": "C",
    "GAU": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "UUU": "F", "UUC": "F",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAU": "H", "CAC": "H",
    "AUA": "I", "AUU": "I", "AUC": "I",
    "AAA": "K", "AAG": "K",
    "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "AUG": "M",
    "AAU": "N", "AAC": "N",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "UGG": "W",
    "UAU": "Y", "UAC": "Y",
    "UAA": "", "UAG": "", "UGA": ""
}


# === Read the text file to a string
with open("/home/amitjavila/Desktop/Courses/rosalind-problems/stronghold/data_8_RNA2prot.txt") as f:
    myRNA = f.read()

# === Run the required code
# Iteratively in windows of 3 nucleotides (for pos in ...)
# We print the key of the RNA codons dictionary that has the value corresponding to that window
myProt = "".join([RNA_Codons[myRNA[pos:pos+3]] for pos in range(0, len(myRNA)-2, 3)])
print(myProt)
