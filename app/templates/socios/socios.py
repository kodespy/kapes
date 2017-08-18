from ...sqlcmd import *
from datetime import datetime

def cargarSocios(filtro):
	if not conectar():
		print("NO hay Conexión")	
	try:
	    conn = psycopg2.connect(CON_STRING)
	except psycopg2.OperationalError as e:
		print('Unable to connect!\n{0}').format(e)
		sys.exit(1)
	else:
		if filtro == 'all':
			filtro = '%%'
		else:
			filtro = '%'+ filtro.upper() +'%'	
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM socios WHERE nombres ILIKE (%s) ORDER BY fecha DESC", (filtro,))
		records = cursor.fetchall()
		return records

def cargarSocio(id):
	if not conectar():
		print("NO hay Conexión")	
	try:
	    conn = psycopg2.connect(CON_STRING)
	except psycopg2.OperationalError as e:
		print('Unable to connect!\n{0}').format(e)
		sys.exit(1)
	else:
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM socios WHERE id=(%s)",(id,))
		row = cursor.fetchone()
		cursor.close()
		return row


		
def guardarSocio(documento, celular, nombres, club,  id, tipo):
	if not conectar():
		print("NO hay Conexión")	
	try:
	    conn = psycopg2.connect(CON_STRING)
	except psycopg2.OperationalError as e:
		print('Unable to connect!\n{0}').format(e)
		sys.exit(1)
	else:
		try:
			fecha = datetime.now()
			cursor = conn.cursor()
			if tipo=='N':
				cursor.execute("INSERT INTO socios (documento, celular, nombres, club, activo) VALUES(%s, %s, %s, %s, %s)", (documento, celular, nombres, club, True))
			else:
				cursor.execute("UPDATE socios SET documento=(%s), celular=(%s), nombres=(%s), club=(%s), fecha=(%s) WHERE id=(%s)", (documento, celular, nombres, club, fecha, id))
			conn.commit()
			return True
		except psycopg2.Error as e:
			flash(e.pgerror, 'danger')
			conn.rollback()
			return False
	finally:			
		conn.close()
def guardarPago(id, monto, mes, tipo, idaporte):
	if not conectar():
		print("NO hay Conexión")	
	try:
	    conn = psycopg2.connect(CON_STRING)
	except psycopg2.OperationalError as e:
		print('Unable to connect!\n{0}').format(e)
		sys.exit(1)
	else:
		try:
			fecha = datetime.now()
			cursor = conn.cursor()
			if tipo=='N':
				cursor.execute("INSERT INTO aportes (idsocio, monto, mes) VALUES(%s, %s, %s)", (id, monto, mes))
			else:
				cursor.execute("UPDATE aportes SET monto=(%s), mes=(%s), fecha=(%s) WHERE id=(%s)", (monto, mes, fecha, idaporte))
			conn.commit()
			return True
		except psycopg2.Error as e:
			flash(e.pgerror, 'danger')
			conn.rollback()
			return False
	finally:			
		conn.close()
def borrarSocio(id):
	if not conectar():
		print("NO hay Conexión")	
	try:
	    conn = psycopg2.connect(CON_STRING)
	except psycopg2.OperationalError as e:
		print('Unable to connect!\n{0}').format(e)
		sys.exit(1)
	else:
		try:
			cursor = conn.cursor()
			cursor.execute("DELETE FROM socio WHERE id=(%s);", (id,))
			conn.commit()
			return True
		except psycopg2.Error as e:
			flash(e.pgerror, 'danger')
			conn.rollback()
			return False
	finally:			
		conn.close()

def cargarAporte(id):
	if not conectar():
		print("NO hay Conexión")	
	try:
	    conn = psycopg2.connect(CON_STRING)
	except psycopg2.OperationalError as e:
		print('Unable to connect!\n{0}').format(e)
		sys.exit(1)
	else:
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM aportes WHERE idsocio=(%s) ORDER BY fecha DESC",(id,))
		records = cursor.fetchall()
		cursor.close()
		return records

def cargarClubes():
	if not conectar():
		print("NO hay Conexión")	
	try:
	    conn = psycopg2.connect(CON_STRING)
	except psycopg2.OperationalError as e:
		print('Unable to connect!\n{0}').format(e)
		sys.exit(1)
	else:
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM clubes")
		records = cursor.fetchall()
		cursor.close()
		return records

