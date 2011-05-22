from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.ext.webapp import template


import os
import cgi
import logging

from encoding import *
from row import Row,rows_from_string

class MainPage(webapp.RequestHandler):
  def get(self):
    rows = Row.all()
    logging.info('Found %d rows',rows.count())
  
    template_vars = {
      'rows': rows,
      'rowcount': rows.count(),
      'sep': cgi.escape(self.request.get("sep")) or ','
    }
    path = os.path.join(os.path.dirname(__file__),"index.html")
    self.response.out.write(template.render(path,template_vars))

  def post(self):
    text = self.request.get('lines')
    sep = self.request.get('sep') or ','
    
    logging.info("line %s - sep %s",text,sep)
    
    rows = rows_from_string(text,sep)
    db.put(rows)
    
    all_rows = Row.all()

    template_vars = {
      'rows': all_rows,
      'rowcount': all_rows.count(),
      'sep': cgi.escape(sep)
    }
      
    path = os.path.join(os.path.dirname(__file__),"index.html")
    self.response.out.write(template.render(path,template_vars))
