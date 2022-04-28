# ROSALIND PROBLEMS

# Bioinformatics stronghold: https://rosalind.info/problems/list-view/

# Problem 5: GC content -----
# https://rosalind.info/problems/gc/

# We are given a FASTA file with a many DNA sequences
# We have to return the ID and GC content of the DNA sequence with highest GC

# === Read data from the file (FASTA formatted file)
# Read the fasta file into a list. 
# Use readlines() and strip() (with readlines() alone there is the \n character also)
with open("/home/amitjavila/Desktop/Courses/rosalind-problems/stronghold/data_5_GCcontent.txt") as f:
    myFASTA = [l.strip() for l in f.readlines()]

# === Clean/Prepare the data (Format for ease of you with our gc_content function)
# Create a dictionary to store the FASTA header as a key and the different lines of sequences as value
# With a for loop, go line by line and add the FASTA header as key (if the line has >) and the following lines as the value.
FASTAdict = {}
FASTAlabel = ""
for line in myFASTA:
    if ">" in line:
        FASTAlabel = line
        FASTAdict[FASTAlabel] = ""
    else:
        FASTAdict[FASTAlabel] += line


# === Format the data (Store the data in a convenient way)
# === Run needed operation on the data (pass the data to our gc_content function)

# Define function to calculate GC content
def gc_content(seq):
    """Computes GC content in a DNA sequence"""
    return (seq.count("C") + seq.count("G")) / len(seq) * 100

# Run the gc_content function on each value of the FASTA dict
# Store the results in another dictionary
GCdict = {key: gc_content(value) for key,value in FASTAdict.items()}

# === Collect results (Rosalind Submission in our case)
# Look the key with max GC content
maxGC = max(GCdict, key = GCdict.get)

# Print the key (without >) and value (in different lines).
print(maxGC[1:] + "\n" + str(GCdict[maxGC]))