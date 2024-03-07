#Question 2: Fibonacci Sequence
#Write a program to generate the Fibonacci sequence up to 100.

def generator_function(up_to_100):
    fibonacci_sequence = [0, 1]

    while True:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        if next_number <= up_to_100:
            fibonacci_sequence.append(next_number)
        else:
            break

    return fibonacci_sequence

fibonacci_sequence = generator_function(100)
print("Fibonacci sequence up to 100:", fibonacci_sequence)
