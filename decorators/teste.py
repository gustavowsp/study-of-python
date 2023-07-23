import doctest

def numeros_inteiros_requeridos(funcao):
  
  def wrapper(x,y):

    if not type(x) == int and not type(x) == float :
      return 'X precisa ser inteiro'
    
    if not type(y) == int and not type(y) == float :
      return 'Y precisa ser inteiro'

    if y < 0:
      return 'Y precisa ser positivo'
    elif x < 0:
      return 'X precisa ser positivo'


    return funcao(x,y)

  return wrapper

@numeros_inteiros_requeridos
def somar_numeros_positivos(x,y):

  return x + y


if __name__ == '__main__':
  doctest.testmod()

  resultado = somar_numeros_positivos(-1,5)
  print(resultado)