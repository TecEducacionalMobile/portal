# -*- coding: utf-8 -*-
import urllib
from utils import *
from Models import models
from google.appengine.api import users
import logging



class AdminHandler(Handler):
	def dispatch(self):
		if not users.is_current_user_admin():
			self.response.out.write("Esta área é restria somente para administradores. Por favor, <a href=" + users.create_login_url('/admin') + "> efetue o seu login.")
		else:
			super(AdminHandler, self).dispatch()

class Admin(AdminHandler):
	def get(self):
		user = users.get_current_user()
		self.render('indexAdmin.html', user = user,loginURL = users.create_login_url('/'),logoutURL = users.create_logout_url('/'))

class Applications(AdminHandler):
	def get(self):
		user = users.get_current_user()
		apps = models.Application.getAllApps(update = True)
		self.render('applicationsAdmin.html', apps = apps, user = user,loginURL = users.create_login_url('/'),logoutURL = users.create_logout_url('/'))


	def post(self):
		user = users.get_current_user()
		apps = models.Application.getAllApps(update = True)
		status = "Success"
		self.characteristics = {}
		for items in ['name','link','device','utility','image','subject','description','installed','free']:
			self.characteristics[items] = self.request.get(items)

		try:
			newApp = models.Application(app_name = self.characteristics['name'],
                             app_image = self.characteristics['image'],
                             app_link = self.characteristics['link'],
                             app_device = self.characteristics['device'],
                             app_utility = self.characteristics['utility'],
                             app_subject = self.characteristics['subject'],
                             app_description = self.characteristics['description'],
                             app_installed = True if self.characteristics['installed'] == 'true' else False,
                             app_free = True if self.characteristics['free'] == 'true' else False)

			newApp.put()
		except:
			status = "Fail"

		self.render("applicationsAdmin.html", apps = models.Application.getAllApps(update = True), createStatus = status, user = user,loginURL = users.create_login_url('/'),logoutURL = users.create_logout_url('/'))

class AppEdit(AdminHandler):
	def get(self, appID):
		user = users.get_current_user()
		try:
			app = models.Application.get(appID)
		except:
			self.render("editApp.html", appFound = False)
		else:
			self.render("editApp.html", app = app, appFound = True)
	def post(self,appID):
		user = users.get_current_user()
		
		app = models.Application.get(appID)
		app.app_name = self.request.get('name')
		app.app_image = self.request.get('image')
		app.app_link = self.request.get('link')
		app.app_device = self.request.get('device')
		app.app_utility = self.request.get('utility')
		app.app_subject = self.request.get('subject')
		app.app_description = self.request.get('description')
		app.app_free = True if self.request.get('free') == 'true' else False
		app.app_installed = True if self.request.get('installed') == 'true' else False
		app.put()
	
		status = "Fail"
		self.render("applicationsAdmin.html", apps = models.Application.getAllApps(update = True), createStatus = status, user = user,loginURL = users.create_login_url('/'),logoutURL = users.create_logout_url('/'))


class Links(AdminHandler):
	def get(self):
		user = users.get_current_user()
		links = models.Links.getLinks(update = True)
		if links:
			self.render('linksAdmin.html', links = links.value)
		else:
			newLinks = models.Links(value="No content added yet")
			newLinks.put()
			self.render('linksAdmin.html', links = newLinks.value)
	def post(self):
		user = users.get_current_user()
		data = self.request.get("content")
		try:
			newLinks = models.Links.getLinks(update = True)
			if newLinks:
				models.Links.changeString(data)
			else:

				models.Links.changeString(data)
		except Exception,e:
			self.response.write(e)
		else:
			self.response.write("As alterações foram salvas com êxito")





