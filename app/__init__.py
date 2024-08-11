from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_manager

#Inicia aplicativo Flask
app = Flask(__name__)

#Token do csrf Forms
app.config['SECRET_KEY'] = '5d27fdf87bfca3986289bc5628d7eba8'

#Cria o DB e diz o caminho onde será alocado.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

#Instância do Banco de dados
db_app = SQLAlchemy(app)

#Criptografia de senha
bycrypt = Bcrypt(app)

#Classe de Login de usuario
#login_manager = LoginManager(app)

#Redireciona se não estiver logado @login_required
#login_manager.login_view = 'login'
#login_manager.login_message = 'Por favor, faça login para acessar essa pagina.'
#login_manager.login_message_category = 'alert-info'

#Roda as URLS de arquivo da aplicação
from app import routes