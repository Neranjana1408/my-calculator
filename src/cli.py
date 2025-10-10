"""
Command Line Interface for Calculator
Example: python src/cli.py add 5 3
"""

import sys
import click
from src.calculator import add, subtract, multiply, divide, power, square_root


@click.command()
@click.argument("operation")
@click.argument("num1", type=float)
@click.argument("num2", type=float, required=False)
def calculate(operation, num1, num2=None):
    """Simple calculator CLI"""
    try:
        if operation == "add":
            if num2 is None:
                click.echo("Addition requires two numbers")
                sys.exit(1)
            result = add(num1, num2)

        elif operation == "subtract":
            if num2 is None:
                click.echo("Subtraction requires two numbers")
                sys.exit(1)
            result = subtract(num1, num2)

        elif operation == "multiply":
            if num2 is None:
                click.echo("Multiplication requires two numbers")
                sys.exit(1)
            result = multiply(num1, num2)

        elif operation == "divide":
            if num2 is None:
                click.echo("Division requires two numbers")
                sys.exit(1)
            if num2 == 0:
                click.echo("Cannot divide by zero")
                sys.exit(1)
            result = divide(num1, num2)

        elif operation == "power":
            if num2 is None:
                click.echo("Power operation requires two numbers")
                sys.exit(1)
            result = power(num1, num2)

        elif operation in ("square_root", "sqrt"):
            result = square_root(num1)

        else:
            click.echo("Unknown operation")
            sys.exit(1)

        # Format output: if result is whole number, show as int
        if isinstance(result, float) and result.is_integer():
            result = int(result)

        print(result, flush=True)
        sys.exit(0)

    except Exception as e:
        click.echo(f"Error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    calculate()
