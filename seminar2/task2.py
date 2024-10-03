def is_even():
    # Input a number
    number = int(input("Input a number: "))

    # Check if the number is even
    if number % 2 == 0:
        return "This is an even number"
    else:
        # If the number is not even, it must be odd
        return "This is an odd number"


# Run the function
print(is_even())
