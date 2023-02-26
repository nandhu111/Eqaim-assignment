def is_valid(number):
    digits = [int(d) for d in str(number)]
    if len(digits) < 2:
        return False
    for i in range(len(digits) - 1):
        if digits[i] >= digits[i+1]:
            return "not Valid"
    return "Valid"

# Examples:
print("189 is",(is_valid(189)))  # Output: True
print("198 is",(is_valid(198)))  # Output: False
print("288 is",(is_valid(288)))  # Output: False
#user input
#n=int(input())
#number=is_valid(n)
#print(n,"is",(number))
