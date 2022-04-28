# ROSALIND PROBLEMS #

# Python village problems: https://rosalind.info/problems/list-view/?location=python-village

# PROBLEM 1 ==========================
# https://rosalind.info/problems/ini1/

# After installing python, type "import this" in the python command line. 
# Copy the text into the solution. 
# Problem one solved

# PROBLEM 2 ==========================
# https://rosalind.info/problems/ini2/

# We want to get the square of the hypothenuse of a triangle with legs a and b

a = 905
b = 913
h = a**2 + b**2
print(h)

# PROBLEM 3 ==========================
# https://rosalind.info/problems/ini3/

# We are given a string with a lot of characters and 4 integers. We want to get two words.
# The integers indicate the start and end position of word 1 and the start and end position of word 2.

myStr = "Sy7N1IybfUkTEbjk1J2uMdrGrammostola9ynsW4o8Dx9rdaufGzeEupn20cY70WaViJGnGncxRX8KmsHbDQ29VwyhddG4rra1XIOVS0fyRwAAxEuY66yNsisXAEaYJnS49cliffordiixovQcmfaLaULhPinoG0afOLfpQex2Sj20j1sgA3eB0"
myInt = [23, 33, 131, 140]
word1 = myStr[myInt[0]:myInt[1]+1]
word2 = myStr[myInt[2]:myInt[3]+1]
print(word1 + " " + word2)
# Result: Grammostola cliffordii

# PROBLEM 4 ==========================
# https://rosalind.info/problems/ini4/

# We are given 2 integers a and b
# We want to get the sum of the odd numbers (1,3...) from a to b, inclusively.

a = 4070
b = 8710

result = 0
for i in range(a,b+1,):
    if i % 2 != 0:
        result = result+i

print(result)


# PROBLEM 5 ==========================
# https://rosalind.info/problems/ini5/

# We are given a file containing up to 1000 lines
# We have to return a file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

# We read the input file into a list, and take the odd positions (indeces in python start in 0, so even lines are odd indices)
# Then we write the lines to a new file

file_in = "/home/amitjavila/Desktop/Courses/rosalind-problems/village/data_problem_5.txt"
with open(file_in) as f:
    file = f.readlines()

text_out = []
for lane in range(len(file)):
    if lane % 2 != 0:
        text_out.append(file[lane])
# print(text_out)

file_out = open("/home/amitjavila/Desktop/Courses/rosalind-problems/village/results_problem_5.txt", "w")
for i in text_out:
    file_out.write(i)
file_out.close()

# PROBLEM 6 ==========================
# https://rosalind.info/problems/ini5/

# We are given a string with up to 1000 letters. Words are separated by spaces.
# Return the number of ocurrences of each word.

myText = "We tried list and we tried dicts also we tried Zen"
myWord = myText.split(' ')
wordCountDict = {}
for word in myWord:
    if word in wordCountDict:
        wordCountDict[word] += 1
    else:
        wordCountDict[word] = 1

# import collections
# wordCountDict = collections.Counter(myWord)

for key, value in wordCountDict.items():
    print(key, value)