# ROSALIND PROBLEMS

# Bioinformatics stronghold: https://rosalind.info/problems/list-view/

# Problem 9: Find DNA motif and the positions where it is found -----
# https://rosalind.info/problems/subs/

# We are given 2 strings of DNA, one is the sequence and the second is the motif to find.
# We have to return the start position of the motif in the sequence (consider 1 as first position of the sequence)


# === Read the text file to a list of strings
with open("/home/amitjavila/Desktop/Courses/rosalind-problems/stronghold/data_9_DNAmotif.txt") as f:
    myDNA = [l.strip() for l in f.readlines()]

seq, motif = myDNA[0], myDNA[1]


# === Run the code
indices = [i+1 for i in range(len(seq)) if seq.startswith(motif, i)]
positions = ' '.join([str(i) for i in indices])
print(positions)