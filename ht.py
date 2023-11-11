from http.server import HTTPServer,BaseHTTPRequestHandler

content= """
<html>
<head>
</head>
<body>
<h1> Krithick Vivekananda </h1>
<h1> Artificial Intelligence and Machine Learning </h1>
</body>
</html>
"""

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(content.encode())

server_address = ('',80)
httpd=HTTPServer(server_address,HelloHandler)
httpd.serve_forever()
