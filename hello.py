from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.ext.webapp import template

from google.appengine.ext.webapp.util import run_wsgi_app

import os
import csv 


class Row(db.Model):
  cols = db.StringListProperty()
  

def rows_from_string(str):
  rd = csv.reader([str],delimiter=',',quotechar='"')
  ret = []
  for row in rd:
    data = Row()
    data.cols = row
    ret = ret + [data]
  
  return ret


  
class MainPage(webapp.RequestHandler):
    def get(self):
      rows = Row.all()
      
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
      
      
        
application = webapp.WSGIApplication(
                                     [('/', MainPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()