from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os, time
import alsaaudio

MIX = alsaaudio.Mixer()

PORT = 8000

FILES = {'./main.css':0}

class SimpleHTTPRequestServer(BaseHTTPRequestHandler):
	def do_GET(self):
		if '/volume/' in self.path:
			print(self.path.split('/')[2])
			MIX.setvolume(int(self.path.split('/')[2]))
		if self.path == "/" :
			f = open(os.path.curdir + os.path.sep + "index.html")
			self.send_response(200)
			self.send_header("Content-type", "text/html")
			self.end_headers()
			self.wfile.write(f.read())
			f.close()
		if self.path == "/update":
			if (FILES['./main.css'] != time.ctime(os.path.getmtime('./main.css'))):
				FILES['./main.css'] = time.ctime(os.path.getmtime('./main.css'))
				self.send_response(0)
				print("update")
			else:
				self.send_response(200)
		if self.path.endswith('.css'):
			f = open(os.path.curdir + os.path.sep + self.path)
			self.send_response(200)
			self.send_header("Content-type", "text/css")
			self.end_headers()
			self.wfile.write(f.read())
			f.close()
		if self.path.endswith('.js'):
			f = open(os.path.curdir + os.path.sep + self.path)
			self.send_response(200)
			self.send_header("Content-type", "text/javascript")
			self.end_headers()
			self.wfile.write(f.read())
			f.close()
		return

server = HTTPServer(('localhost', PORT), SimpleHTTPRequestServer)

#save pid in .pid
os.system('echo '+ str(os.getpid()) + ' > .pid')

server.serve_forever()