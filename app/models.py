from app import db
from sqlalchemy.dialects import postgresql
from sqlalchemy.dialects.postgresql.json import JSONB
#from sqlalchemy.ext.indexable import index_property
from sqlalchemy import UniqueConstraint
from sqlalchemy import Index, MetaData, Table, Column, Integer, TypeDecorator, Text, DateTime
from sqlalchemy.orm import validates
from datetime import datetime
from sqlalchemy.sql import func



class Socios(db.Model):
    __tablename__ = 'socios'

    id = db.Column(db.Integer, primary_key=True)
    documento = db.Column(db.Integer, unique=True)
    nombres = db.Column(db.String())
    celular = db.Column(db.String())
    club = db.Column(db.String())
    admin = db.Column(db.Boolean(), default=False)
    fecha = db.Column(DateTime(timezone=True), server_default=func.now())
    activo = db.Column(db.Boolean(), default=True)
    
    def __init__(self, nombre):
        self.nombres = nombres

    def __repr__(self):
        return '<id {}>'.format(self.id)

class Aportes(db.Model):
    __tablename__ = 'aportes'

    id = db.Column(db.Integer, primary_key=True)
    idsocio =  db.Column(db.Integer, db.ForeignKey('socios.id'))
    monto =  db.Column(db.Integer)
    mes =  db.Column(db.String)
    fecha = db.Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return '<id {}>'.format(self.id)

class Clubes(db.Model):
    __tablename__ = 'clubes'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, unique=True)
    def __repr__(self):
        return '<id {}>'.format(self.id)        