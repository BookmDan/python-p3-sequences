#!/usr/bin/env python3

def print_fibonacci(length):
    # fib_seq = [0,1]
    # while len(fib_seq) < length:
    #     next = fib_seq[-1] + fib_seq[-2]
    #     fib_seq.append(next)

    # print(fib_seq)
    fibonacci_sequence = []
    a, b = 0, 1

    for _ in range(length):
        fibonacci_sequence.append(a)
        a, b = b, a + b

    print(f'{fibonacci_sequence}')