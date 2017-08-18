from flask import Flask

from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from .sqlcmd import *
#from .templates.empresas.empresas import *

import datetime
import json

from app import app



@app.route('/')
def index():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
	if session.get('logged_in'):
		return index()
	else:	
		cedula = request.form['_documento']
		socio = verSocio(cedula) 
		if socio != None:
			rol = socio[5]
			activo = socio[7]
			if (not activo ):
				flash('No se pudo realizar la autenticación del Socio... SOCIO INACTIVO', 'danger')
				return index()
			session['idusuario'] = socio[0]	
			session['usuario'] = socio
			session['logged_in'] = True
			session['admin'] = rol
			return index()
		else:
			flash('No se pudo realizar la autenticación del Socio...', 'danger')
			return index()

@app.route("/logout")
def logout():
	if session.get('logged_in') == True:
		session['logged_in'] = False
		session['usuario'] = None
	return index()


@app.errorhandler(404)
def not_found(error):
  return render_template('404.html'), 404			