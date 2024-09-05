# server.py
import http.server
import socketserver


class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello from PSPDFKit Engineer!")


PORT = 8000


def run_server():
    with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
        print(f"Serving on port {PORT}\n")
        httpd.serve_forever()


if __name__ == "__main__":
    run_server()
