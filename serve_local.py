#!/usr/bin/env python3
"""
Local development server with CSP headers for Giscus support
"""
import http.server
import socketserver
import os
from pathlib import Path

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Set CSP headers to allow Giscus and MyST CDN resources
        self.send_header('Content-Security-Policy', 
            "default-src 'self'; "
            "script-src 'self' 'unsafe-inline' 'unsafe-eval' https://giscus.app https://*.giscus.app https://cdn.jsdelivr.net https://cdnjs.cloudflare.com; "
            "style-src 'self' 'unsafe-inline' https://giscus.app https://*.giscus.app https://github.githubassets.com https://cdn.jsdelivr.net https://cdnjs.cloudflare.com; "
            "frame-src https://giscus.app https://*.giscus.app; "
            "connect-src 'self' https://giscus.app https://*.giscus.app https://api.github.com https://github.com; "
            "img-src 'self' data: https: blob:; "
            "font-src 'self' data: https: https://cdnjs.cloudflare.com;"
        )
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('X-XSS-Protection', '1; mode=block')
        super().end_headers()

def main():
    PORT = 8000
    html_dir = Path("_build/html")
    
    if not html_dir.exists():
        print(f"❌ Directory {html_dir} not found!")
        print("Please run 'myst build --html' first.")
        return
    
    os.chdir(html_dir)
    
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        print(f"🚀 Server running at http://localhost:{PORT}/")
        print("💬 Giscus comments enabled with proper CSP headers")
        print("📍 Press Ctrl+C to stop the server")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n✅ Server stopped")

if __name__ == "__main__":
    main()

