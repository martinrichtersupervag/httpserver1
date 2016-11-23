# server_main 23.11.2016
# projekt httpserver1
# testovani pythonu a napsani vlastniho serveru
# - vytvoreni serveru, napsani jednoducheho index.html
# - zatim se nedari vytvorit spojeni https

import http.server
import ssl

httpd = http.server.HTTPServer(('localhost', 443), http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, certfile='c:\Prog\python\TestUtils\httpserver1\hrcserver.pem', server_side=True, keyfile='c:\Prog\python\TestUtils\httpserver1\hrcserverkey.pem')
httpd.serve_forever()