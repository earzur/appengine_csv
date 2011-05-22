from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.ext.webapp import template

import os
import cgi
import logging

import encoding

from row import Row

class CSVHandler(webapp.RequestHandler):
  def get(self):
    rows = Row.all()
    logging.info('CSV requested. Found %d rows',rows.count())
    if rows.count() > 0:
      self.response.headers['Content-Type'] = "application/csv"
      writer = encoding.UnicodeWriter(self.response.out,delimiter=cgi.escape(self.request.get("sep").__str__()),quotechar='"')
      for row in rows:
        writer.writerow(row.cols)
    else:
      print "Content-Type: text/html"
      print
      print "<h1>No data to display ...</h1>"
      
