# Number of Fibonacci elements
n = 50

# Fibonacci series
fibonacci_series = [0, 1]

# Use lambda to generate the next Fibonacci number and append it
fibonacci = lambda seq: seq.append(seq[-2] + seq[-1])

# Generate Fibonacci sequence using a loop
for _ in range(2, n):
    fibonacci(fibonacci_series)

print(fibonacci_series)
