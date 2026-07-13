# server.py
from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/')
def serve_file():
    # Serve the file as an attachment or inline
    return send_file('hello.txt', as_attachment=False)

if __name__ == '__main__':
    # Render sets the PORT environment variable
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
