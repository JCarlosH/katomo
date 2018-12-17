#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, MySQLdb

class DBManager():

	HOSTNAME = ''
	USERNAME = ''
	PASSWORD = ''
	DATABASE = ''
	PORT     = ''
	SOCKET   = ''

	__connection = None
	__cursor     = None

	""" 
	Metodos principales que gestionan la parte mas importante del proyecto
	que es el manejo de la base de datos con los debidos metodos.
	"""
	def __connectioToMySQL(self):
		try:
			self.__connection = MySQLdb.Connection(self.HOSTNAME,self.USERNAME,self.PASSWORD,self.DATABASE)
			self.__cursor = self.__connection.cursor()
		except MySQLdb.Error, e:
			return e

	def __closeConnection(self):
		self.__connection.close()
		self.__cursor.close()

	def __getQueryResult(self,query):
		"""
        Procesa la peticio que se envia
        :param str query:		sentencia SQL
        """
		try:
			self.__connectioToMySQL()
			self.__cursor.execute(query)
			result = self.__cursor.fetchall()
			self.__closeConnection()
			return result
		except MySQLdb.Error, e:
			return e

	def _executeQueryResult(self,query):
		try:
			self.__connectioToMySQL()
			self.__cursor.execute(query)
			self.__connection.commit()
			self.__closeConnection()
		except MySQLdb.Error, e:
			return e

	"""
	Metodos asociados para el manejo de datos dentro de la bd
	todos son para la administracion.
	"""
	def showDatabases(self):
		return self.__getQueryResult('SHOW DATABASES;')

	def useDatabase(self,database):
		return self.__getQueryResult('USE ' + database + ';')

	def createDatabase(self,name):
		return self.__getQueryResult('CREATE DATABASE '+ name + ' CHARACTER SET utf8 COLLATE utf8_general_ci;')

	def dropDatabase(self,name):
		return self.__getQueryResult('DROP DATABASE ' + name + ';')

	"""
	Metodos asociado con el manejo de tablas dentro de la base de datos
	"""
	def showTables(self):
		return self.__getQueryResult('SHOW TABLES')
		