def add_numbers(num1, num2):
    carry = ""
    sum_str1=""
    carry1=0
    steps = {}
    for i in range(max(len(str(num1))-1,len(str(num2)))):
        # Extract digits from both numbers at same place value
        digit1 = int(str(num1)[-i-1]) if i < len(str(num1)) else 0
        digit2 = int(str(num2)[-i-1]) if i < len(str(num2)) else 0

        # Add digits along with carry from previous step
        digit_sum = digit1 + digit2+carry1

        # Compute carry and sum strings for this step
        carry_str = carry+"1"
        sum_str = str(digit_sum % 10)
        sum_str1=sum_str+sum_str1

        # Add step to the dictionary
        steps[f"step{i+1}"] = {"carryString":carry_str, "sumString": sum_str1}

        # Update carry for next step
        carry = carry+"1"
        carry1=(digit_sum//10)
        
        

    # Add final step with the full sum
    steps[f"step{len(steps)+1}"] = {"carryString": str(carry), "sumString": str(num1 + num2)}

    # Return the steps as a JSON object
    print(steps)

# Example usage
num1 = 1489
num2 = 714
steps = add_numbers(num1, num2)
