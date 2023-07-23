from calculadora import somar

try:
  valor_somado = somar(15,15)
  print('Função soma funcionando')
except AssertionError as error:
  print(f'\nConta inválida "{error}"\n')

  