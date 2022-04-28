# ROSALIND PROBLEMS

# Bioinformatics stronghold: https://rosalind.info/problems/list-view/

# Problem 1: Counting DNA nucleotides 
# https://rosalind.info/problems/dna/

# Function to count nucleotides (list of A C G T nucleotides)
def countNucFreq(seq):

    NucFreqDict =  {"A":0, "C":0, "G":0, "T":0}
    for nuc in seq:
        NucFreqDict[nuc] += 1
    
    NucFreq = ' '.join([str(val) for key, val in NucFreqDict.items()])

    return NucFreq


# PROBLEM -------
# Download the sample data
# Copy the DNA string or read it.
problem_file = open("/home/amitjavila/Desktop/Courses/rosalind-problems/stronghold/rosalind_dna.txt", "r")
rosalind_dna = problem_file.read()
problem_file.close()

# Call the function countNucFreq()
rosalind_dna_freq = countNucFreq(rosalind_dna)

# Print the result
print(rosalind_dna_freq)

# solution: 217 209 207 202