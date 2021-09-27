from sys import stderr


def safe_print_integer_err(value):
    try:
        print('{:d}'.format(value))
        return True
    except Exception as err:
        print('Exception: {:s}'.format(str(err)), file=stderr)
        return False
