import os
import re
import random
import hashlib
import urllib
import hmac
import logging
from string import letters

import webapp2
import jinja2
import logging
from google.appengine.api import memcache
from google.appengine.ext import db
from google.appengine.api import mail
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext import blobstore
from Models import models

template_dir = os.path.join(os.path.dirname(__file__), '../templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)

secret = "fart"


def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)


def make_secure_val(val):
    return '%s|%s' % (val, hmac.new(secret, val).hexdigest())


def check_secure_val(secure_val):
    val = secure_val.split('|')[0]
    if secure_val == make_secure_val(val):
        return val


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def logged(self):
        return True if self.read_secure_cookie('logged') == 'YES' else False

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def set_secure_cookie(self, name, val):
        cookie_val = make_secure_val(val)
        self.response.headers.add_header(
            'Set-Cookie',
            '%s=%s; Path=/' % (name, cookie_val))

    def set_inexpirable_cookie(self, name, val):
        cookie_val = make_secure_val(val)
        self.response.headers.add_header(
            'Set-Cookie',
            '%s=%s; expires=Fri, 01-Jan-2112 23:59:59 GMT; Path=/' % (name, cookie_val))

    def read_secure_cookie(self, name):
        cookie_val = self.request.cookies.get(name)
        return cookie_val and check_secure_val(cookie_val)

class createApp(Handler):
    def get(self):
        self.render("createApp.html")
    def post(self):
        self.characteristics = {}
        for items in ['name','link','device','utility','subject','description','installed','free','image']:
            self.characteristics[items] = self.request.get(items)
        newApp = models.Application(app_name = self.characteristics['name'],
                             app_image = self.characteristics['image'],
                             app_link = self.characteristics['link'],
                             app_device = self.characteristics['device'],
                             app_utility = self.characteristics['utility'],
                             app_subject = self.characteristics['subject'],
                             app_description = self.characteristics['description'],
                             app_installed = True,
                             app_free = True)
        newApp.put()
        self.redirect('/applications')

class createTutorial(Handler):
    def get(self):
        self.render("createTutorial.html")
    def post(self):
        self.characteristics = {}
        for items in ['name','image_link','link','description','instructor']:
            self.characteristics[items] = self.request.get(items)
        tutorial = models.Tutorial(name = self.characteristics['name'],
                                 link = self.characteristics['link'],
                                 image_link = self.characteristics['image_link'],
                                 description = self.characteristics['description'],
                                 instructor = self.characteristics['instructor'])
        tutorial.put()
        self.redirect('/tutorials')







