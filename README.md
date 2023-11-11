# Ex-01-Simple-Web-Server
###### Name: Krithick Vivekananda 
###### Ref.No: 23009445
## Date:11/11/23


## AIM:
To develop a simple webserver to serve html pages.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

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


# OUTPUT:

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
```python
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

```


## OUTPUT:
![out](webserver.jpg)

## RESULT:
The program for implementing simple webserver is executed successfully.
