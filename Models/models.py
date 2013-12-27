# -*- coding: utf-8 -*-
from google.appengine.api import memcache
from google.appengine.ext import db
from google.appengine.api import mail
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext import blobstore

class Tutorial(db.Model):
    name = db.StringProperty(required=True)
    image_link = db.StringProperty()
    link = db.StringProperty()
    description = db.StringProperty()
    instructor = db.StringProperty(required = True)

    @classmethod
    def getAllTutorials(cls, update = False):
        key = 'all_tutorials'
        if not update:
            result = memcache.get(key)
            if result:
                return result
            else:
                result = Tutorial.all()
                memcache.set(key,result)
                return result
        else:
            result = Tutorial.all()
            memcache.set(key,result)
            return result

class Application(db.Model):
    app_name = db.StringProperty(required=True)
    app_image = db.StringProperty()
    app_link = db.StringProperty()
    app_device = db.StringProperty()
    app_utility = db.StringProperty()
    app_subject = db.StringProperty()
    app_description = db.StringProperty()
    app_installed = db.BooleanProperty()
    app_free = db.BooleanProperty()

    @classmethod
    def getAllApps(cls, update = False):
        key = 'all_apps'
        if not update:
            result = memcache.get(key)
            if result is not None:
                return result
            else:
                result = Application.all()
                memcache.set(key,result)
                return result
        else:
            result = Application.all()
            memcache.set(key,result)
            return result

class Links(db.Model):
    value = db.TextProperty()

    @classmethod
    def getLinks(cls, update = False):
        key = 'links'
        if not update:
            result = memcache.get(key)
            if result is not None:
                return result
            else:
                result = Links.all().get()
                memcache.add(key,result)
                return result
        else:
            result = Links.all().get()
            memcache.set(key,result)
            return result

    @classmethod
    def changeString(cls, data):
        currentVal = Links.all().get()
        currentVal.value = db.Text(data)
        currentVal.put()




