from http.server import HTTPServer, BaseHTTPRequestHandler
import requests

class ProxyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Asli site ka content uthate hain
        url = "http://demo.testfire.net"
        response = requests.get(url)
        
        # Poora page mita kar 10,000 baar Raju ❤️ Babita likhte hain
        banner = "Raju ❤️ Babita " * 10000
        custom_html = f"""
        <html>
        <body style='background:black; color:#ff69b4; font-family:cursive; word-wrap:break-word; margin:0; padding:20px;'>
            <h1 style='font-size:50px; text-align:center; text-shadow:0 0 20px pink;'>PRICELSSYNC DOMINANCE</h1>
            <p style='font-size:12px; opacity:0.8;'>{banner}</p>
        </body>
        </html>
        """
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(custom_html.encode())

print("[+] PRICELSSYNC Proxy Server starting on port 8080...")
HTTPServer(('0.0.0.0', 8080), ProxyHandler).serve_forever()
