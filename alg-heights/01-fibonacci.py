# ROSALIND PROBLEMS

# Algorithmic heights: https://rosalind.info/problems/list-view/?location=algorithmic-heights

# Problem 1: Fibonacci numbers -----
# https://rosalind.info/problems/fibo/

# More information about Fibonacci sequence in: https://www.mathsisfun.com/numbers/fibonacci-sequence.html
# Simplified, in the Fibonacci sequence, the next number is obtained by summing the 2 last numbers of the sequence, e.g., 0,1,1,2,3,5,8,13,21...

# We are given a positive integer (n).
# We have to return the number in the n position of the Fibonacci sequence.


# === Function for the Fibonacci sequence
# Initial list with the 2 first Fibonacci numbers (0 and 1)
# Then iterate through the position 3 (index 2) to the specified position
# For each position, append the sum of the last two numbers
def fibonacci(generations = 3):
    fibo = [0,1]
    for i in range(2,generations+1,1):
        fibo.append((fibo[i-2]+fibo[i-1]))
    return fibo

# === Run the function with the given integer and return the last value
myInt = 22
myFibo = fibonacci(myInt)
print(myFibo[-1])

