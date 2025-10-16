# Importa la funzione Flask da flask
# Secondo commento
from flask import Flask

# Crea un istanza della classe Flask
app = Flask(__name__)

# Viene creato un collegamento tra la URL e la funzione hello_world
@app.route('/')
def hello_world():
    # Ritorna 'Hello, World'
    return 'Hello, World!'

# La app è in running in modalità debug, utile durante lo sviluppo per catturare errori
if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 5000)