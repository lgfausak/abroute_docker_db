#!/usr/bin/env python2

import web
import subprocess

urls = (
        "/(dbinit.*)", "dbinit"
    )

class dbinit:
    def GET(self, path):
#        rv = subprocess.check_output("abinit",stderr=subprocess.STDOUT,shell=True)
        rv = 'not doing anything here'
        return rv

class index:
    def GET(self, path):
        return 'Hello ' + path

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
