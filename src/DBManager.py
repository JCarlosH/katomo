#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, MySQLdb

"""
TODO
[x] Empezar a programar :v
[] Documentar todo el codigo
[] Hacer todos los metodos relacionados a la manipulacion de la base de datos
[] Hacer testing 
"""

class DBManager():

	HOSTNAME = ''
	USERNAME = ''
	PASSWORD = ''
	DATABASE = ''
	PORT     = ''
	SOCKET   = ''

	_connection = None
	_cursor     = None

	""" 
	Metodos principales que gestionan la parte mas importante del proyecto
	que es el manejo de la base de datos con los debidos metodos.
	"""
	def _connectioToMySQL(self):
		try:
			self._connection = MySQLdb.Connection(self.HOSTNAME,self.USERNAME,self.PASSWORD,self.DATABASE)
			self._cursor = self._connection.cursor()
		except MySQLdb.Error, e:
			return e

	def _closeConnection(self):
		self._connection.close()
		self._cursor.close()

	def _getQueryResult(self,query):
		"""
        Procesa la peticio que se envia
        :param str query:		sentencia SQL
        """
		try:
			self._connectioToMySQL()
			self._cursor.execute(query)
			result = self._cursor.fetchall()
			self._closeConnection()
			return result
		except MySQLdb.Error, e:
			return e

	def _executeQueryResult(self,query):
		try:
			self._connectioToMySQL()
			self._cursor.execute(query)
			self._connection.commit()
			self._closeConnection()
		except MySQLdb.Error, e:
			return e

	"""
	Metodos asociados para el manejo de datos dentro de la bd
	todos son para la administracion.
	"""
	def showDatabases(self):
		return self._getQueryResult('SHOW DATABASES;')

	def useDatabase(self,database):
		return self._getQueryResult('USE ' + database + ';')

	def createDatabase(self,name):
		return self._getQueryResult('CREATE DATABASE '+ name + ' CHARACTER SET utf8 COLLATE utf8_general_ci;')

	def dropDatabase(self,name):
		return self._getQueryResult('DROP DATABASE ' + name + ';')

	"""
	Metodos asociado con el manejo de tablas dentro de la base de datos
	"""
	def showTables(self):
		pass

	def createTable(self,name,**arg):
		e = """
		CREATE TABLE PRODUCTOS();
		"""
		pass
		