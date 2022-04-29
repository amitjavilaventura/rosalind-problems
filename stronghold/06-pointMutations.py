# ROSALIND PROBLEMS

# Bioinformatics stronghold: https://rosalind.info/problems/list-view/

# Problem 6: Point Mutations -----
# https://rosalind.info/problems/hamm/

# We are given two DNA sequences of equal length
# We have to return the hamming distance (number of nucleotides that differ between the two sequences)

with open("/home/amitjavila/Desktop/Courses/rosalind-problems/stronghold/data_6_pointMutations.txt") as f:
    seqs = f.readlines()

hamm = 0
for i in range(len(seqs[0])-1):
    if seqs[0][i] != seqs[1][i]:
        hamm += 1

print(hamm)

