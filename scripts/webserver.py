#!/usr/bin/env python

import os
import SimpleHTTPServer

def kill():
    os.system("kill -KILL " + str(os.getpid()))

os.chdir(os.path.dirname(__file__) + "/../contents")
SimpleHTTPServer.test()
