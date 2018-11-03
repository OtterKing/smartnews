import webapp2
import jinja2
import os
import json
from google.appengine.api import urlfetch
import sdk
import re

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)