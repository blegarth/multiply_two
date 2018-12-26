# -*- coding: utf-8 -*-

"""Console script for multiply_two."""
import sys
import click


@click.command()
@click.argument('num1', metavar='number1')
@click.argument('num2', metavar='number2')
def main(num1, num2):
    """This is a example command that multiplies number1 and number2"""
    if not (num1.isnumeric() or num2.isnumeric()):
        click.echo('The expected arguments should be integers')
    else:
        click.echo('The answer is: ' + str(int(num1)*int(num2)))
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
