from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
from .sqlcmd import *
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = os.urandom(29)
app.static_folder = 'static'
app.jinja_env.cache = {}
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)


# import tables ---
from .models import Socios
from .models import Aportes
from .models import Clubes


#existEmpresa("80035140-1")
# Vistass
from app import views
from .templates.socios import views
#from .templates.empresas import views
#from .templates.sucursales import views


