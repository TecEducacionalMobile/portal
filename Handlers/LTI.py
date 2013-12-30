# -*- coding: utf-8 -*-
from utils import *
from Models import models
from google.appengine.api import users
import urllib
import logging

class launchLTI(Handler):
	def get(self):
		felp = {'a': 'Janice Joplin'}
		string = urllib.urlencode(felp)
		answer = "<html><body><a href=/launchLTI?"+ string + ">Someting</a></body></html>" + self.request.get('a')
		self.response.out.write(answer)
		# self.logged = True
		# if self.logged:
		# 	self.set_secure_cookie('logged','YES')
		# 	self.set_secure_cookie('roles', self.request.get('roles').encode('utf-8'))
		# 	self.set_secure_cookie('email', self.request.get('lis_person_contact_email_primary').encode('utf-8'))
		# 	self.set_secure_cookie('course', self.request.get('context_title').encode('utf-8'))  
		# 	self.set_secure_cookie('name', self.request.get('list_person_name_full').encode('utf-8')) 
	def post(self):
		felp = {'a': 'óção'}
		string = urllib.urlencode(felp)
		self.response.out.write("<html><body>"+ string + ">Someting</a></body></html>")
		# params = {}
		# if 'Administrator' in self.request.get('roles'):
		# 	answer = "AQUI EM BREVE O NOVO SISTEMA DE RESERVA INTEGRADO NO MOBILE VIRTUAL. ABAIXO SEGUEM OS DETALHES DA SUA CONTA <br> Para mais esclarecimentos, entre em contato em tec.educacional@escolamobile.com.br <br><br><br> "
		# 	for attribute in ['context_title','custom_canvas_course_id','lis_person_contact_email_primary','lis_person_name_full','roles','user_image']:
		# 		params[attribute]=self.request.get(attribute)
		# 	for item in params:
		# 		answer += item + ' : ' + params[item] + " <br>"
		# 	self.response.out.write(answer)
		# else:


		# 	for attribute in['context_title','lis_person_contact_email_primary','lis_person_name_full']:
		# 		params[attribute]=self.request.get(attribute)
		# 	self.redirect('/reserva',params)

		# self.logged = True 
		# if self.logged:
		# 	self.set_inexpirable_cookie('logged','YES')
		# 	self.set_secure_cookie('roles', self.request.get('roles').encode('utf-8'))
		# 	self.set_secure_cookie('email', self.request.get('lis_person_contact_email_primary').encode('utf-8'))
		# 	self.set_secure_cookie('course', self.request.get('context_title').encode('utf-8'))  
		# 	self.set_secure_cookie('name', self.request.get('list_person_name_full').encode('utf-8')) 
		# self.redirect("/")