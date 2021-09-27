def safe_print_division(a, b):
    r = None
    try:
        r = a / b
    finally:
        print('{}'.format(r))
        return r
