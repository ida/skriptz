# This is a copy of:
# http://www.codegist.net/snippet/python/plone_reloadpy_shylux_python
# Huge thanks to "shylux".


from __future__ import print_function
import sys
import re
import requests
 
 
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
 
domain = 'localhost'
port = 8080
user = 'admin'
pw = 'admin'
 
url = 'http://{0}:{1}/reload?action=code'.format(domain, port)
url = 'http://{0}:{1}/Plone'.format(domain, port)
 
try:
    req = requests.get(url, auth=(user, pw))
except requests.exceptions.ConnectionError:
    print('No zope running on {}:{}'.format(domain, port))
    exit()
 
if req.status_code == 200:
 
    if b'Code reloaded:' in req._content:
        print('Code reloaded', req.status_code)
    elif b'No code reloaded!' in req._content:
        print('No code reloaded', req.status_code)
    else:
        eprint('Strange content', req._content)
elif req.status_code == 401:
    eprint('Unauthorized', req.status_code)
 
elif b'<h2>Site Error</h2>' in req._content:
    eprint('YOUR CODE SUCKS', req.status_code)
else:
    eprint('Error', req.status_code)

