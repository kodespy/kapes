from flask import Flask
from flask import flash
import psycopg2
import sys
import pprint
import socket
from .config import SQLALCHEMY_DATABASE_URI


CON_STRING = SQLALCHEMY_DATABASE_URI

#Obtener dirección de IP
def pcIp():
	addr = socket.gethostbyname(socket.gethostname())
	return addr

def conectar():
	try:
   		conn = psycopg2.connect(CON_STRING)
	except psycopg2.OperationalError as e:
   		print('No se pudo conectar con el Servidor!\n{0}').format(e)
   		return False
	else:
		return True

def verSocio(cedula):
	if not conectar():
		print("NO hay Conexión")	
	try:
	    conn = psycopg2.connect(CON_STRING)
	except psycopg2.OperationalError as e:
		print('Unable to connect!\n{0}').format(e)
		sys.exit(1)
	else:
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM socios WHERE documento = (%s)", (cedula,))
		row = cursor.fetchone()
		cursor.close()
		return row
