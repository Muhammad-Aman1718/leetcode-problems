# Find_GCD_and_LCM


def findGCD(a: int, b: int):
    """Function to calculate GCD using brute force method"""

    # Start from the smaller number
    min_num = min(a, b)

    # Check from min_num down to 1
    for i in range(min_num, 0, -1):

        # Check if i divides both
        if a % i == 0 and b % i == 0:

            # Largest common divisor found
            return i

    # If no other divisor is found, GCD is 1
    return 1


def findLCM(a: int, b: int):
    """Function to calculate LCM using brute force method"""

    # Start from the larger number
    max_num = max(a, b)
    while True:

        # Check if max_num is a multiple of both
        if max_num % a == 0 and max_num % b == 0:

            # Smallest common multiple found
            return max_num

        # Try next number
        max_num += 1


# Input two numbers
num1, num2 = map(int, input("Enter two numbers: ").split())

# Calculate GCD and LCM using brute force
gcd = findGCD(num1, num2)
lcm = findLCM(num1, num2)

# Output results
print(f"GCD of {num1} and {num2} is: {gcd}")
print(f"LCM of {num1} and {num2} is: {lcm}")
