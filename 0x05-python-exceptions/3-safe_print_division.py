#!/usr/bin/python3
def safe_print_division(a, b):
    r = None
    try:
        r = a / b
    except ValueError:
        return None
    except r == 0:
        return None
    finally:
        print("Inside result: {}".format(r))
        return r
