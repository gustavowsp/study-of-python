def somar(primeiro_numero : int | float, segundo_numero : int | float) -> int | float:
    """Soma primeiro_numero e segundo_numero
    >>> somar(10,20)
    30
    >>> somar('5',10)
    Traceback (most recent call last):
    ...
    AssertionError: O primeiro_numero precisa ser INT ou FLOAT
    """


    # Validando os parâmetros
    assert isinstance(primeiro_numero,(int,float)), 'O primeiro_numero precisa ser INT ou FLOAT'
    assert isinstance(segundo_numero,(int,float)), 'O segundo_numero precisa ser INT ou FLOAT'

    return primeiro_numero + segundo_numero

def subtrair(x : int | float, y: int | float) -> int | float:
    """Subtração de x e y
    >>> subtrair(5,5)
    0
    >>> subtrair(5,'sdasd')
    Traceback (most recent call last):
    ...
    AssertionError: X deve ser do tipo "INT" ou FLOAT
    """


    # Validando os parâmetros
    assert isinstance(x, (int,float)), 'X deve ser do tipo "INT" ou "FLOAT"'
    assert isinstance(y, (int,float)), 'X deve ser do tipo "INT" ou FLOAT'

    return x - y

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)