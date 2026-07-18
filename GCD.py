numberLargest = int(input("Enter Largest number : "))
numberSmallest = int(input("Enter Smallest number :"))

while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

print("HCF is : ",numberLargest)


def decimal_to_base(num,base):
    if num == 0:
        return "0"
    
    digits = "0123456789ABCDEF"
    result = ""

    while num > 0:
        remainder = num % base
        result = digits[remainder] + result
        num = num // base

    return result

print(decimal_to_base(25,2))
print(decimal_to_base(254,16))


def base_to_decimal(num_str,base):
    digits = "0123456789ABCDEF"
    decimal_val = 0
    power = 0

    for char in num_str[::-1]:
        digit_value = digits.index(char.upper())
        decimal_val += digit_value * (base ** power)
        power += 1

    return decimal_val

print(base_to_decimal("11001",2))
print(base_to_decimal("FE",16))