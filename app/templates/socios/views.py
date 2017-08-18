from flask import Flask

from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from app import *
from ...sqlcmd import *
from .socios import *

# Operaciones con Ciudades
@app.route('/socios/<filtro>')
def socios(filtro):
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		try:
			data = cargarSocios(filtro)
			return render_template('/socios/lista.html', list=data)
		except Exception as e:
			return render_template('index.html')    
@app.route('/socio/agregar')
def agregarsocio():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		clubes = cargarClubes()
		return render_template('/socios/agregar.html', list=clubes)

@app.route('/socio/editar/<id>')
def editarsocio(id):
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		data = cargarSocio(id)
		clubes = cargarClubes()
		return render_template('/socios/editar.html', data=data, list=clubes)

@app.route('/socio/pago/<id>')
def pagosocio(id):
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		data = cargarSocio(id)
		return render_template('/socios/pago.html', data=data)

@app.route('/socio/balance/<id>')
def balancesocio(id):
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		data = cargarSocio(id)
		data1 = cargarAporte(id)
		return render_template('/socios/balance.html', data=data, list=data1)
@app.route('/guardarsocio', methods=['POST']) 
def guardarsocio():
	if request.method == 'POST':
		tipo = request.form['_tipo']
		if tipo == 'N':
			id = 0
		else:
			id = request.form['_id']
		documento	= request.form['_documento']
		nombres	= request.form['_nombres']
		celular	= request.form['_telefono']
		club	= request.form['_clubes']
		if guardarSocio(documento, celular, nombres, club, id, tipo):
			return socios("all")
		else:
			return render_template('/socios/agregar.html')
@app.route('/guardaraporte', methods=['POST']) 
def guardaraporte():
	if request.method == 'POST':
		tipo = request.form['_tipo']
		id = request.form['_id']
		idaporte = request.form['_idaporte']
		monto	= request.form['_monto']
		mes	= request.form['_mes']
		if guardarPago(id, monto, mes, tipo, idaporte):
			return socios("all")
		else:
			data = cargarSocio(id)
			return render_template('/socios/pago.html', data=data)
@app.route('/borrarsocio/<id>')
def borrarsocio(id):
	borrarSocio(id)
	return socios('all')