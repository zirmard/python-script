
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

terms = int(input("How many terms in the Fibonacci sequence? "))
for i in range(terms):
    print(fibonacci(i), end=" ")
    