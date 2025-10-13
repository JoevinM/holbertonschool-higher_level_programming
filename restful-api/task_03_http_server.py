#!/usr/bin/env python3
"""
Simple HTTP server using http.server.

This script creates a minimal API with multiple endpoints
to demonstrate how to handle GET requests and return
different types of responses (plain text, JSON, etc.)
using only Python’s standard library.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class subclass(BaseHTTPRequestHandler):
    """
    Custom request handler class for the simple API.

    This class defines responses for various GET endpoints:
    - `/` : Returns a welcome message.
    - `/data` : Returns JSON sample data.
    - `/status` : Returns a simple status message.
    - `/info` : Returns API version and description.
    - Any other path : Returns a 404 error.
    """

    def do_GET(self):
        """
        Handle GET requests for defined endpoints.
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data)
            self.wfile.write(json_data.encode())

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"ok")

        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"version": "1.0", "description":
                    "A simple API built with http.server"}
            json_data = json.dumps(data)
            self.wfile.write(json_data.encode())

        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer, handler_class=subclass):
    """
    Start the HTTP server on port 8000.

    Args:
        server_class (HTTPServer): The HTTP server class.
        handler_class (BaseHTTPRequestHandler): The request handler class.
    """
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Serving on port 8000...")
    httpd.serve_forever()


if __name__ == '__main__':
    run()
