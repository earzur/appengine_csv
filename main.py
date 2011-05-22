from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.ext.webapp import template


import os
import logging

from encoding import *
from row import Row

class MainPage(webapp.RequestHandler):
  def get(self):
    rows = Row.all()
    logging.info('Found %d rows',rows.count())
  
    template_vars = {
      'rows': rows
    }
    path = os.path.join(os.path.dirname(__file__),"index.html")
    self.response.out.write(template.render(path,template_vars))

  def post(self):
    text = self.request.get('lines')
    
    rows = rows_from_string(text)
    db.put(rows)
    
    all_rows = Row.all()

    template_vars = {
      'rows': all_rows
    }
      
    path = os.path.join(os.path.dirname(__file__),"index.html")
    self.response.out.write(template.render(path,template_vars))
