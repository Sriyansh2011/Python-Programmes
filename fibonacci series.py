def print_fibonacci(x):
    a, b = 0, 1
    if x <= 0:
        print("Please enter a positive integer.")
    elif x == 1:
        print(f"Fibonacci series up to {x} term: {a}")
    else:
        print(f"Fibonacci series up to {x} terms:")
        count = 0
        while count < x:
            print(a, end=" ")
            nth = a + b
            a = b
            b = nth
            count += 1
terms = int(input("How many terms? "))
print_fibonacci(terms)