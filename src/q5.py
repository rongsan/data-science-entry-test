def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    # Check if both num and divisor are numeric.
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        print("Error: Both num and divisor must be numeric.")
        return

    res_bool = False

    # Check if the number (num) is divisible by another number (divisor)
    if num % divisor == 0:
      res_bool = True
      
    return res_bool


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

print(check_divisibility(10, 2)) # Expected: True
print(check_divisibility(7, 3))   # Expected: False
