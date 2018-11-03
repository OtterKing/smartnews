import webapp2
import jinja2
import os
import json
from google.appengine.api import urlfetch
import re

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


def hello_world():
	print("hello world")
	hello = "hello_world"

class HelloWorld(webapp2.RedirectHandler):
	def get(self):
		#main_template = the_jinja_env.get_template('template/popup.html')
		#self.response.write(main_template.render())
	def post(self):
	    main_template2 = the_jinja_env.get_template('template/popup2.html')
	    self.response.write(main_template2.render())

app = webapp2.WSGIApplication([
    ('/', HelloWorld)
    ], debug=True)


