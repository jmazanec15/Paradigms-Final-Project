import cherrypy
from databasecontroller import databaseController
from _planets_database import _planets_database
import re
import json

def start_service():
	dispatcher = cherrypy.dispatch.RoutesDispatcher()

	mydb = _planets_database()
	mydb.load_planets('oec.csv')
	databasecontroller = databaseController(mydb)


	dispatcher.connect('planet_get' , '/planets/', controller = databasecontroller, action = 'GET' , conditions=dict(method=['GET']))
	dispatcher.connect('planet_get_pid', '/planets/:pid', controller=databasecontroller, action = 'GET_PID', conditions=dict(method=['GET']))
	dispatcher.connect('planet_put_pid', '/planets/:pid', controller=databasecontroller, action = 'PUT', conditions=dict(method=['PUT']))
	dispatcher.connect('planet_delete', '/planets/', controller=databasecontroller, action = 'DELETE', conditions=dict(method=['DELETE']))
	dispatcher.connect('planet_delete_pid' , '/planets/:pid' , controller=databasecontroller, action ='DELETE_PID' , conditions=dict(method=['DELETE']))
	dispatcher.connect('scaled_get' , '/planets/scaled/:pid' , controller=databasecontroller, action ='GET_SCALED' , conditions=dict(method=['GET']))
	dispatcher.connect('reset' , '/planets/reset' , controller=databasecontroller, action ='POST' , conditions=dict(method=['POST']))

	conf = { 'global' : {'server.socket_host': 'student04.cse.nd.edu','server.socket_port': 51020 } , '/' : {'request.dispatch': dispatcher} }

	cherrypy.config.update(conf)
	app = cherrypy.tree.mount(None,config=conf)


	cherrypy.quickstart(app)

	


if __name__ == '__main__':
	start_service()


	