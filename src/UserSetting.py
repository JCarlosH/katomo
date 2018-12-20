#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

class UserSetting():
	def __init__(self):
		with open('src/config/preferences.json','r') as file:
			self.data = json.load(file)

		#print(self.data)

	def languaje(self,change = ''):
		if change == '':
			return self.data['lang']
		else:
			self.data['lang'] = change

	def excludeDB(self,change = ''):
		if change == '':
			return self.data['excludedb']
		else:
			self.data['excludedb'] = change

	def returnData(self):
		return self.data

	def countConnections(self):
		conn = self.data['connections']
		n = len(conn.keys())
		if n == 0:
			return 0
		else:
			return n

	def deleteConnections(self,connection):
		self.data['connections'].pop(connection)

	def addConnection(self,llave,*arreglo):
		datos = arreglo
		self.data['connections'][llave] = {u'username':datos[0],u'password':datos[1],u'hostname':datos[2]}

	def writeData(self):
		print(self.data)
		try:
			with open('src/config/preferences.json','w') as file:
				json.dump(self.data,file)
		except Exception as e:
			return e

"""
us = UserSetting()

print(us.countConnections())
print(us.deleteConnections('concon2'))
print(us.countConnections())

print(us.countConnections())
us.addConnection('mconexion','juan','23456','localhost')
us.writeData()
print(us.countConnections())

"""