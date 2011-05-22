from google.appengine.ext import db

from encoding import unicode_csv_reader
import logging

class Row(db.Model):
  cols = db.StringListProperty()


def rows_from_string(str,sep=','):
  logging.info("rows_from_string('%s','%s') set of type %s",str,sep,type(sep))
  rd = unicode_csv_reader(str.splitlines(),delimiter=sep.__str__(),quotechar='"')
  ret = []
  for row in rd:
    data = Row()
    data.cols = row
    ret = ret + [data]

  return ret
  
  