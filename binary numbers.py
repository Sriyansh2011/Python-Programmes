binary = input("Enter a binary number: ")

decimal = 0
length = len(binary)

for i in range(length):
    digit = int(binary[length - 1 - i])
    decimal = decimal + digit * (2 ** i)

print("Decimal Number =", decimal)