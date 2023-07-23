import unittest
from calculadora import somar

class TesteModuloCalculadora(unittest.TestCase):
    
    def test_soma_varias_saidas(self):
      
      x_y_saidas = (
        (10,20,30),
        (0,20,20),
        (-10,20,10),
        (-20,20,0),
        (20,-20,0),
        (1.,2.5,3.5),
      )

      for x_y_saida in x_y_saidas:

        # Checando se x + y é igual a saida, caso não vamos exibir as entradas.
        with self.subTest(x_y_saida=x_y_saida):
          x, y, saida = x_y_saida
          self.assertEqual(somar(x, y), saida)

    def test_soma_se_numeros_nao_sao_int(self):

      entradas = (
        ('primeiro_numero',10),
        (10,'segundo_numero')
      ) 
      
      for entrada in entradas:
        primeiro_numero, segundo_numero = entrada

        with self.assertRaises(AssertionError):
          somar(primeiro_numero,segundo_numero)


unittest.main(verbosity=2)