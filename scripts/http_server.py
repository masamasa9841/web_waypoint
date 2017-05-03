#!/usr/bin/env python
# coding: utf-8

import argparse
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class JsonResponsehandler(BaseHTTPRequestHandler):
    def __set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self.__set_headers()
        f = open("../contents/index.html", "r")
        self.wfile.write(f.read())

    def do_HEAD(self):
        self.__set_headers()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="usage:set http server port as '--port 8080' or '-p 8080'")
    parser.add_argument("-p", "--port", type=int, default=8080, help="define tcp port of http server")
    args = parser.parse_args()

    server = HTTPServer(("", args.port), JsonResponsehandler)
    print "server running on port " + str(args.port)
    server.serve_forever()
