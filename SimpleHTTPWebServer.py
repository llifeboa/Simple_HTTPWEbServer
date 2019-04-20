from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os, time

PORT = 8080

FILES = {'./main.css':0}

class SimpleHTTPRequestServer(BaseHTTPRequestHandler):
	def do_GET(self):
		if self.path == "/" :
			f = open(os.path.curdir + os.path.sep + "index.html")
			print(os.path.curdir + os.path.sep + "index.html")
			self.send_response(200)
			self.send_header("Content-type", "text/html")
			self.end_headers()
			self.wfile.write(f.read())
			f.close();
		if self.path == "/update":
			print(FILES['./main.css'])
			print(time.ctime(os.path.getmtime('./main.css')))
			print(FILES['./main.css'] == time.ctime(os.path.getmtime('./main.css')))
			if (FILES['./main.css'] != time.ctime(os.path.getmtime('./main.css'))):
				FILES['./main.css'] = time.ctime(os.path.getmtime('./main.css'))
				self.send_response(0)
			else:
				self.send_response(200)
			print(self.send_response)
		if self.path.endswith('.css'):
			f = open(os.path.curdir + os.path.sep + self.path)
			print(os.path.curdir + os.path.sep + self.path)
			self.send_response(200)
			self.send_header("Content-type", "text/css")
			self.end_headers()
			self.wfile.write(f.read())
			f.close();
		return

try:
	server = HTTPServer(('localhost', PORT), SimpleHTTPRequestServer)
	print (server.server_address)
	server.serve_forever()
except KeyboardInterrupt:
	server.socket.close()