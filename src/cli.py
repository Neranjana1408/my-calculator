"""
Command Line Interface for Calculator
Example: python src/cli.py add 5 3
"""

import sys
import traceback
import click
from src.calculator import add, subtract, multiply, divide, square_root


@click.command()
@click.argument("operation")
@click.argument("num1", type=float)
@click.argument("num2", type=float, required=False)
def calculate(operation, num1, num2=None):
    """Simple calculator CLI"""
    try:
        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            result = divide(num1, num2)
            result = round(result, 2)
        elif operation == "square_root":
            result = square_root(num1)
        else:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)

        # Format result — remove trailing .0 for whole numbers
        click.echo(str(int(result)) if result == int(result) else str(result))

    except TypeError as error:
        click.echo(f"Unexpected error: {error}")
        sys.exit(1)

    except ZeroDivisionError as error:
        click.echo(f"Error: {error}")
        sys.exit(1)

    except ValueError as error:
        click.echo(f"Error: {error}")
        sys.exit(1)

    # 👇 This block is optional, but good for debugging
    except Exception as error:
        click.echo("Unexpected internal error. Please contact support.")
        # Print full traceback to stderr for debugging
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":  # pylint: disable=no-value-forparameter
    calculate()
