#!/usr/bin/env python3

modules_path = 'answers'

"""

basic python server

If you ask for '[hostname]/about', the server will look for a Python-file of same name in the 'answers'-directory.

If the Python-file contains a 'main'-method, it will be executed upon the request-object and send its return back to the browser.

If you sended data alongside, e.g. through a web-form, you can retrieve it off the request's 'data'-attribute, see './answers/index.py' for an example.

If you ask for '[hostname]/about.html', the server will look for './answers/about.html' and send its content back to the browser.

Same goes for '[hostname]/about.json', '[hostname]/about.css', '[hostname]/about.txt', '[hostname]/about.jpg' and any other file-type.


"""



from http.server import BaseHTTPRequestHandler, HTTPServer
from importlib import import_module
from mimetypes import guess_type as get_type
from os.path import exists
from urllib.parse import parse_qs as parse_to_dict
import shutil


class MyHandler(BaseHTTPRequestHandler):
  
    def do_GET(self):
        module = None
        message = 'Nothing found for ' + self.path
        status = 404
        content_type = 'text/html'
        rel_path = self.path[1:]
        rel_path = rel_path.split('?')[0]
        if rel_path == '': rel_path = 'index'
        file_path = modules_path + '/' + rel_path
        print('file_path is ./' + file_path)
        if exists(file_path):
            content_type = get_type(rel_path)[0]
            self.send_response(200)
            self.send_header('Content-type', content_type)
            self.end_headers()
            with open(file_path, 'rb') as fil:
                shutil.copyfileobj(fil, self.wfile)
        elif exists(file_path + '.py'):
            module = import_module(modules_path + '.' + rel_path)
            if 'main' in dir(module):
                message = module.main(self)
            self.send_message(message, status, content_type)
        else:
            self.send_message(message, status, content_type)

        
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        data = self.rfile.read(length).decode('utf-8')
        self.data = parse_to_dict(data)
        self.do_GET()

    def send_message(self, message, status=200, content_type='text/html'):
        status = 200
        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.end_headers()
        message = self.genHtml(message)
        self.wfile.write(bytes(message, 'utf8')) #write text

    def genHtml(self, message):
        return '''<style>
        @media (prefers-color-scheme: dark) {
            body {
                background: black;
                color: white;
            }
        }

        </style>''' + message


def main():
    print('Starting server on port 8081')
    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()


if __name__ == '__main__':
    main()
