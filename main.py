def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return "0"
    binary_number = ""
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_number = str(remainder) + binary_number
        decimal_number = decimal_number // 2
    return binary_number

# Example usage
decimal_number = int(input("Enter a decimal number: "))
print(f"Binary representation: {decimal_to_binary(decimal_number)}")



    
