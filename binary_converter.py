import random
choice = [0,1]

# generate a random binary number
def random_binary():
    # generate a random binary number
    random_digits = []
    # generate 4 random digits
    for i in range(4):
        random_choice = random.choices(choice)
        random_digits.append(random_choice)
        # turn the list of lists into a single list
        single_list = [item for sublist in random_digits for item in sublist]
        single_list = "".join(str(x) for x in single_list)
    return (single_list)

# turn a binary into base 10
def binary_to_decimal(binary):
    # convert binary to decimal
    decimal = 0
    binary_length = len(binary)
    # loop through the binary digits
    for digit in binary:
        # convert the digit to an integer
        #decimal = decimal*2 + int(digit)
        decimal += int(digit) * (2**(binary_length - 1))
        binary_length -= 1
    return decimal

print(binary_to_decimal(random_binary()))

# Write a program to sum the first 50 fibonacci sequence