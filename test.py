import webapp2
import jinja2
import json
import os
from flask import Flask

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HelloWorld(webapp2.RedirectHandler):
	def get(self):
		main_template = jinja_current_directory.get_template('template/popup.html')
		self.response.write(main_template.render())

	def post(self):
		user_info = self.request.get("name")
	    main_template2 = jinja_current_directory.get_template("template/popup2.html")
	    self.response.write(main_template2.render())



app = Flask(__name__)
@app.route('/')
def print_hello():
    return 'Hello World'
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

app = webapp2.WSGIApplication([
    ('/', HelloWorld, HelloWorld2)
    ], debug=True)

start_template=jinja_current_directory.get_template