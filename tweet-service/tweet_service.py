import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

# Sample data storage
tweets = []

class TweetHandler(BaseHTTPRequestHandler):
    # Handle GET requests
    def do_GET(self):
        if self.path == "/tweets":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            # Convert tweets list to JSON and send it
            self.wfile.write(json.dumps(tweets).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    # Handle POST requests
    def do_POST(self):
        if self.path == "/tweets":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            new_tweet = json.loads(post_data.decode("utf-8"))
            # Retrieve user information from User Service
            user_id = new_tweet["userId"]
            print(f"new_tweet{new_tweet}")
            print(f"user_id{user_id}")
           
            user_info = requests.get(f"http://user-service:3001/users/{user_id}")
            if user_info.status_code == 200:
                # Parse JSON data and add it to the tweets list
                
                tweets.append(new_tweet)

                self.send_response(201)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                # Confirmation message
                self.wfile.write(json.dumps({"message": "Tweet created"}).encode("utf-8"))
            else:
                self.send_response(404)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

# Server setup
def run(server_class=HTTPServer, handler_class=TweetHandler):
    server_address = ('', 3002)
    httpd = server_class(server_address, handler_class)
    print("Tweet Service running on port 3002...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
