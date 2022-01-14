import os

from flask import Flask

def create_app(test_config=None):
    #Criação e configuração do app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )


    if test_config is None:
        #Carregar a instância de configuração, se ela existir, quando não estiver testando
        app.config.from_pyfile('config.py', silent=True)
    else:
        #Carrega a configuração de teste se passada como entrada
        app.config.from_pyfile(test_config)


    #Verifica se a pasta da instância existe
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    #Uma simples página para dizer Hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'


    return app
