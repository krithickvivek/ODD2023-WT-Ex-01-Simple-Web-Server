from http.server import HTTPServer,BaseHTTPRequestHandler

content= """
<html>
<head>
</head>
<body>
<h1>Top Three Web Application Develpoment Frameworks </h1>
<h3>1.Django</h3>
<h3>2.MEAN Stack</h3>
<h3>3.React</h3>
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
