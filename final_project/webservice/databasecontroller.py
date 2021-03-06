#Andrew Callahan
#CherryPy Primer

import cherrypy
import re
import json


class databaseController(object):
	def __init__(self, mydb):
		self.mydb=mydb
	def OPTIONS(self, *args, **kargs):
	    return ""
	def GET(self):
		output = {'result':'success'}
		try:
			planets = self.mydb.get_planets()
			output['planets'] = planets
		except KeyError as ex:
			output['result'] = 'error'
		return json.dumps(output)

	def GET_PID(self,pid):
		output = dict()
		try:
			output = self.mydb.get_planet(pid)
			output['result'] = 'success'
		except:
			output = {'result':'error', 'message':'wrong input'}
		return json.dumps(output)

	def DELETE(self):
		output = {'result' : 'success'}
		try:
			self.mydb.delete_planets()
		except:
			output = {'result':'error', 'message':'key not found'}
		return json.dumps(output)

	def DELETE_PID(self, pid):
		output = {'result':'success'}
		try:
			self.mydb.delete_planet(pid)
		except:
			output = {'result':'error'}
		return json.dumps(output)
	def PUT(self, pid):
		cl = cherrypy.request.headers['Content-Length']
		rawbody = cherrypy.request.body.read(int(cl))
		body = json.loads(rawbody)
		output = {'result': 'success'}
		try:
			self.mydb.set_planet(pid,body)
		except:
			output = {'result':'failure'}
		return json.dumps(output)
	def POST(self):
		output = {'result':'success'}
		try:
			self.mydb.load_planets('oec.csv')
		except:
			output = {'result':'error', 'message':'key not found'}
		return json.dumps(output)
	def GET_SCALED(self,pid):
		output = dict()
		try:
			output = self.mydb.get_planet(pid)
			output['scaled_to_earth'] = self.mydb.scale_to_earth(pid)
			output['result'] = 'success'
		except:
			output = {'result':'error', 'message':'wrong input'}
		return json.dumps(output)



