# -*- coding: utf-8 -*-
from utils import *
from Models import models
from google.appengine.api import users
import logging



class Principal(Handler):
	def get(self):
		user = users.get_current_user()
		self.render('index.html',user = user,loginURL = users.create_login_url('/'),logoutURL = users.create_logout_url('/'))

class Reserva(Handler):
	def get(self):
		user = users.get_current_user()
		params = {}
		self.render('ipadReservation.html',params = self.request.params, user = user,loginURL = users.create_login_url('/'),logoutURL = users.create_logout_url('/'))

class IpadReservation(Handler):
	def get(self):
		show = ""
		for key in self.request.params:
			show += "key: " + key + " Val: " + self.request.params[key]
		self.response.out.write(show)
		# user = users.get_current_user()
		# if self.request.get('reserved') == 'true':
		# 	self.render('iPadConfirmationPage.html')
		# else:
		# 	params = {}
		# 	params['name'] = self.request.get()

		# 	self.render('iPadReservationForm.html',params = params)

class Applications(Handler):
	def get(self):
		self.redirect('/applications/list')

class Application(Handler):
	def get(self,app_id):
		self.redirect('/applications/list')

class AppList(Handler):
	def get(self):
		user = users.get_current_user()
		apps = models.Application.getAllApps()
		self.render("applist.html", apps = apps, user = user,loginURL = users.create_login_url('/'),logoutURL = users.create_logout_url('/'))

	def post(self):
		user = users.get_current_user()
		device = self.request.get('device')
		subject = self.request.get('subject')
		utility = self.request.get('utility')
		free = self.request.get('free')
		q = models.Application.getAllApps()
		if device != "Todos":
			q.filter('app_device =', device)
		if subject != "Todos":
			q.filter('app_subject =', subject)
		if utility != "Todos":
			q.filter('app_utility =', utility)
		if free != "Todos":
			if free == "Sim":
				q.filter('app_free =', True)
			else:
				q.filter('app_free =', False)

		self.render("applist.html", apps = q, user = user,loginURL = users.create_login_url('/'),logoutURL = users.create_logout_url('/'))

class Forum(Handler):
	def get(self):
		user = users.get_current_user()
		self.render('ipadReservation.html',user = user,loginURL = users.create_login_url('/'),logoutURL = users.create_logout_url('/'))

class Tutorials(Handler):
	def get(self):
		user = users.get_current_user()
		self.render('tutorials.html',tutorials = models.Tutorial.getAllTutorials(), user = user,loginURL = users.create_login_url('/'),logoutURL = users.create_logout_url('/'))

class PopulateFields(Handler):
	def get(self):
		exampleApp = models.Application(app_name = "Exemplo",
										app_link = "http://www.google.com",
										app_device = "Web",
										app_subject = "Biologia",
										app_utility = "Audio",
										app_description = "Breve Descrifdo do Aplicativo",
										app_free = False,
										app_installed = True)
		exampleApp.put()
		exampleTutorial = models.Tutorial(name = "Como produzir uma Video Aula",
										  image_link = "http://placehold.it/300x200",
										 link = "http://coccosproxy.appspot.com/iba",
										 description = "a light description here",
										 instructor = "Felipe Cocco")
		exampleTutorial.put()
		self.response.out.write("Added Successfully!")

class Links(Handler):
	def get(self):
		user = users.get_current_user()
		self.render('links.html')

