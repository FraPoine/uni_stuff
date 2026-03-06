from http.server import BaseHTTPRequestHandler, HTTPServer
PORT = 8000
REDIRECT_URL = "http://localhost:5000/admin"
class RedirectHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(302)
        self.send_header('Location', REDIRECT_URL)
        self.end_headers()
def run_server():
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, RedirectHandler)
    print(F'Server running on port {PORT}...')
    httpd.serve_forever()
    
if __name__ == '__main__':
    run_server()