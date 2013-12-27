# -*- coding: utf-8 -*-
from utils import *
from Models import models
from google.appengine.api import users
import logging

class reservaLTI(Handler):
	def post(self):
		params = {}
		if 'Administrator' not in self.request.get('roles'):
			answer = "AQUI EM BREVE O NOVO SISTEMA DE RESERVA INTEGRADO NO MOBILE VIRTUAL. ABAIXO SEGUEM OS DETALHES DA SUA CONTA <br> Para mais esclarecimentos, entre em contato em tec.educacional@escolamobile.com.br <br><br><br> "
			for attribute in ['context_title','custom_canvas_course_id','lis_person_contact_email_primary','lis_person_name_full','roles','user_image']:
				params[attribute]=self.request.get(attribute)
			for item in params:
				answer += item + ' : ' + params[item] + " <br>"
			self.response.out.write(answer)
		else:


			for attribute in['context_title','lis_person_contact_email_primary','lis_person_name_full']:
				params[attribute]=self.request.get(attribute)
			self.redirect('/reserva',params)