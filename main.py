#!/usr/bin/env python
import random

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from datetime import datetime


class RandomHandler(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(str(datetime.now().microsecond) + str(int(random.random() * 1000)))

class ParamHandler(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(self.request.get("val"))

class HeaderHandler(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'

        header_value = self.request.get("val")

        self.response.headers['custom-header'] = header_value
        self.response.out.write("set 'custom-header' to " + header_value)

def main():
    application = webapp.WSGIApplication([
                                          ('/random', RandomHandler),
                                          ('/param', ParamHandler),
                                          ('/header', HeaderHandler)
                                         ],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
