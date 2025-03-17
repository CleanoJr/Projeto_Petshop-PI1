from flask import Flask
from flask_session import Session

# Criação de uma instância do Flask
app = Flask(__name__)

# Chave secreta para criptografar a sessão
app.config['SECRET_KEY'] = 'minha_chave_secreta'

# Configuração da sessão para armazenar no lado do servidor
app.config['SESSION_TYPE'] = 'filesystem'

Session(app)

from controllers.usuario_controller import *
from controllers.cliente_controller import *
from controllers.pet_controller import *
from controllers.funcionario_controller import *

#Inicia o servidor de desenvolvimento.
if __name__ == '__main__':
    app.run()