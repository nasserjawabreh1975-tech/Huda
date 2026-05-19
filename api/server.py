from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

os.chdir("../ui")

server = HTTPServer(("0.0.0.0", 8090), SimpleHTTPRequestHandler)

print("HUDA UI ONLINE : http://0.0.0.0:8090")

server.serve_forever()
