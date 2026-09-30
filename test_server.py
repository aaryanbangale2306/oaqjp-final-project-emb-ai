"""
Simple HTTP server for testing the Emotion Detection interface.
Uses Python standard library - no external dependencies required.
"""

import http.server
import socketserver
import json
from urllib.parse import urlparse, parse_qs
import sys
import os
import threading
import time

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from EmotionDetection.emotion_detection import emotion_detector


class EmotionDetectionHandler(http.server.BaseHTTPRequestHandler):
    """HTTP Request Handler for Emotion Detection API"""

    def do_GET(self):
        """Handle GET requests"""
        if self.path == "/" or self.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            
            # Read and send index.html
            try:
                with open("templates/index.html", "r", encoding="utf-8") as f:
                    self.wfile.write(f.read().encode())
            except FileNotFoundError:
                self.wfile.write(b"<h1>Emotion Detection Interface</h1>")
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Not found"}).encode())

    def do_POST(self):
        """Handle POST requests"""
        if self.path == "/emotion_detection":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode()
            
            try:
                request_data = json.loads(body)
                text = request_data.get("textToAnalyze", "").strip()
                
                if not text:
                    self.send_response(400)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(
                        json.dumps(
                            {"error": "Invalid text! Please enter some text."}
                        ).encode()
                    )
                    return
                
                result = emotion_detector(text)
                
                if result is None:
                    self.send_response(400)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(
                        json.dumps(
                            {"error": "Invalid text! Please enter some text."}
                        ).encode()
                    )
                    return
                
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(result).encode())
                
            except json.JSONDecodeError:
                self.send_response(400)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(
                    json.dumps({"error": "Invalid JSON"}).encode()
                )
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Not found"}).encode())

    def log_message(self, format, *args):
        """Suppress logging"""
        pass


def run_server(port=5000, duration=5):
    """Run the HTTP server for testing"""
    handler = EmotionDetectionHandler
    
    try:
        with socketserver.TCPServer(("", port), handler) as httpd:
            print(f"Server running on http://localhost:{port}")
            print(f"Will run for {duration} seconds...")
            
            # Run server in a thread
            server_thread = threading.Thread(target=httpd.serve_forever)
            server_thread.daemon = True
            server_thread.start()
            
            # Run for specified duration
            time.sleep(duration)
            
            httpd.shutdown()
            print("Server stopped")
            
    except OSError as e:
        print(f"Error starting server: {e}")


if __name__ == "__main__":
    run_server(port=5000, duration=30)
