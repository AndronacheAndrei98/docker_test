import http.server
import socketserver

PORT = 8080

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        html = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Docker Debugging - Task 5</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    text-align: center;
                }
                .success {
                    color: green;
                    font-size: 24px;
                    margin: 20px 0;
                }
            </style>
        </head>
        <body>
            <h1>Docker Debugging Assignment</h1>
            <h2>Day 1 - Task 5</h2>
            <div class="success">
                Success! You've fixed the missing file issue!
            </div>
            <p>
                You successfully fixed the Dockerfile by creating the missing requirements.txt file.
            </p>
        </body>
        </html>
        '''
        
        self.wfile.write(html.encode())

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever() 