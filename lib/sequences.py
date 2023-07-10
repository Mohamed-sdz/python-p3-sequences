#!/usr/bin/env python3
def print_fibonacci(length):
    fibonacci_sequence = []
    x, y = 0, 1

    for _ in range(length):
        fibonacci_sequence.append(x)
        x, y = y, x + y

    print(fibonacci_sequence)
