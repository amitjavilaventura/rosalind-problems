# ROSALIND PROBLEMS

# Bioinformatics stronghold: https://rosalind.info/problems/list-view/

# Problem 4: Rabbits and recurrence -----
# https://rosalind.info/problems/fib/

# This problem is linked to the Fibonacci sequence.

# A explanation to this problem can be found here:
# https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbmRPVFFMajJFMnlBT2IybHN4TmhWTThORVlfQXxBQ3Jtc0ttOExlQk9aUW40MTlrWFNKMm50ZzQ0WFhmbUFMdndRdUtsc0ZBZjdXS0IyVzFveVNITlUzV3U2R2k4Y0QxNGNMTkY4bnFxOHZySFp4Slc3SW9pQlYzeHRpLXZXYVNDUjVuYXliLTZSOER6YTlhcmZvSQ&q=https%3A%2F%2Fmedium.com%2Falgorithms-for-life%2Frosalind-walkthrough-rabbits-and-recurrence-relations-4812c0c2ddb3&v=3eBIHdyGJLQ
# https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbW9MNWlXNmlOcW95S2lnZlN0WTdVd0xkejljZ3xBQ3Jtc0tsYlIzX0dGbW5vRjRrRmQ2QUdFZTRsUGpId0VWaWtnZXhpQTlmSXo3OE5HZXdoQWhjamU1b1lHV2RyVkZ6MkNoUWFBd0hWSmUzVmVudENhdU96ZGlpdFpKUGtCRVNMMXZOZnpuZG14OXduUlk4T0lhWQ&q=https%3A%2F%2Fchrispresso.coffee%2F2019%2F02%2F21%2Frosalind-rabbits-and-recurrence-relations%2F&v=3eBIHdyGJLQ

# We have a certain number of rabits.
# We are given a number of months (generations of the Fibonacci loop) and the number of offspring obtained by rabbit in each generation
# We have to return the last number of the iteration.

# The function defined in our Fibonacci problem https://rosalind.info/problems/fibo/ is not valid, but can be useful.

# === Define the function to calculate the offspring of the rabits.

# def rabbitsOffspring(months, offspring):
    # if months == 0: return 0
    # parent, children = 1, 1
    # for i in range(months-1):
    #     children, parent = parent, parent + children*offspring
    # return children

def rabbitsOffspring(months, offspring):
    rabbits = [0,1]
    for i in range(2,months+1,1):
        rabbits.append( rabbits[i-1] + rabbits[i-2]*offspring  )
    return rabbits


# === Run the function with the given data and print the last value
# Our data is 30 2
print(rabbitsOffspring(30,2)[-1])