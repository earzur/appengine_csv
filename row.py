from google.appengine.ext import db

class Row(db.Model):
  cols = db.StringListProperty()
