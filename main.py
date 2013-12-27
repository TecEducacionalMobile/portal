#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import webapp2
import logging
from Handlers import Classroom
from Handlers import Home
from Handlers import utils
from Handlers import Admin
from Handlers import LTI

def handle_404(request, response, exception):
    logging.exception(exception)
    response.write('Render HTML with resource error')
    response.set_status(404)

app = webapp2.WSGIApplication([('/', Home.Principal),
							   ('/admin',Admin.Admin),
							   ('/ipadReservationForm',Home.IpadReservation),
							   ('/applicationsAdmin',Admin.Applications),
							   ('/applications/edit/(.*)', Admin.AppEdit),
							   ('/createApp',utils.createApp),
							   ('/createTutorial',utils.createTutorial),
	                           ('/applications',Home.Applications),
	                           ('/applications/list',Home.AppList),
	                           ('/applications/(\d+)',Home.Application),
	                           ('/reserva',Home.Reserva),
	                           ('/reservaLTI',LTI.reservaLTI),
	                           ('/populate',Home.PopulateFields),
	                           ('/links',Home.Links),
	                           ('/linksAdmin',Admin.Links),
	                           ('/tutorials',Home.Tutorials)], debug=True)

app.error_handlers[404] = handle_404
