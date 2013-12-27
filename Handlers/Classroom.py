from utils import *
from Models import models
import logging


class Classroom(Handler):
    def get(self):
        # self.render("classroom.html")
        self.render("idetest.html")
    def post(self):
        logging.error(self.request.POST)
        self.response.out.write('[{"iId":"1","heading":"Management Services","body":"<h1>Program Overview</h1><h1>January 29, 2009</h1>"}]')
