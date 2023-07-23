from flask import Flask
import doctest

app = Flask(__name__)

@app.route("/")
def hello_word():
    """
    >>> hello_word()
    '<h1>Hello Word</h1>'
    """
    return(
      '<h1>Hello Word</h1>'
      )

@app.route("/teste/")
def teste():
    return('<h1>Teste</h1>')

if __name__ == '__main__':
    doctest.testmod()