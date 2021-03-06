#!/usr/bin/python3
"""
Programt to div a matrix
the elements should be a matrix
return the div of the elementes of matrix
"""


def matrix_divided(matrix, div):
    """Programt to div a matrix
    the elements should be a matrix
    return the div of the elementes of matrix"""

    m = []
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    for i in matrix:
        if len(i) == 0:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        else:
            m.append(len(i))
        for x in i:
            if type(x) is not float and type(x) is not int:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
    if len(set(m)) != 1:
        raise TypeError('Each row of the matrix must have the same size')
    if type(div) is float or type(div) is int:
        pass
    else:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return [[round(x/div, 2) for x in j] for j in matrix]
