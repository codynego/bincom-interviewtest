# The sum of the first 50 fibonacci sequence numbers

def fibonacci_sum(n=50):
    # Initialize the fibonacci sequence
    fibonacci_sequence = [0, 1]
    # Finding the sum of the first 50 fibonacci sequence numbers
    for i in range(2, n):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    return sum(fibonacci_sequence)

print(fibonacci_sum())
