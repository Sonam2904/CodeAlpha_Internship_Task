# Ask the user how many Fibonacci numbers they want
n = int(input("How many Fibonacci numbers do you want? "))

# Initializing the first two numbers in the sequence
a = 0
b = 1

# Using a third variable to hold the next number
for _ in range(n):
    print(a)  
    c = a + b  # Calculate the next number
    a = b  
    b = c  
