"""
Calculator Module - Basic arithmetic operations
Students will extend this with more functions
"""


def add(num1, num2):  # pylint: disable=invalid-name
    """Add two numbers together"""
    return num1 + num2


def subtract(num1, num2):
    """Subtract b from a"""
    return num1 - num2


def multiply(num1, num2):
    """Multiply two numbers with input validation"""
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return num1 * num2


def divide(num1, num2):
    """Divide a by b with error handling"""
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("Division requires numeric inputs")
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2


def power(num1, num2):
    """Raise a to the power of b"""
    # FIX: Corrected the redundant type check on num1 to check num2
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("Power function requires numeric inputs")
    return num1**num2


def square_root(num1):
    """Calculate square root of a"""
    if not isinstance(num1, (int, float)):
        raise TypeError("Square root requires a numeric input")
    if num1 < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return num1**0.5


if __name__ == "__main__":
    print("🧮 Calculator Module")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"4 × 2 = {multiply(4, 2)}")
    print(f"9 ÷ 3 = {divide(9, 3)}")
    print(f"2 ^ 3 = {power(2, 3)}")
    print(f"√16 = {square_root(16)}")
