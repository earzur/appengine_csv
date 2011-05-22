from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from main import MainPage
from csv_handler import CSVHandler

application = webapp.WSGIApplication(
                                     [ ('/csv',CSVHandler),
                                       ('/', MainPage) ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()