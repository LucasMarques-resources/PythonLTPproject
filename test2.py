def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

print(has_numbers("I own 1 dog"))
# True
print(has_numbers("I own no dog"))
# False