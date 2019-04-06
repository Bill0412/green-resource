import http.server as server
import json



class MyHandler(server.BaseHTTPRequestHandler):
	data_file_name = 'data.json'


	# (core) Handler for the POST request
	def do_POST(self):
		#content_len = int(self.headers.get('Content_length'))
		#post_body = self.rfile.read(content_len)


		# JSON
		self.data = self.rfile.read().decode()

		print('data:\n', self.data)

		# write data to file
		with open(self.data_file_name, 'w') as out:
			json.dump(self.data, out)


	# Handler for the GET request
	# host the webpage for the info
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		# Send the html message

		
		with open(self.data_file_name, 'r') as infile:
			self.data = json.load(infile)

		print(self.data)
		print(type(self.data))
		self.wfile.write(self.data.encode())
		



def run(server_class=server.HTTPServer, handler_class=server.BaseHTTPRequestHandler):
    server_address = ('0.0.0.0', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run(handler_class=MyHandler)