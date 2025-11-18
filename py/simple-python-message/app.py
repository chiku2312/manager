# app.py
from flask import Flask, Response
import os

app = Flask(__name__)

MESSAGE_FILE = os.path.join(os.path.dirname(__file__), "message.txt")

def read_message():
    try:
        with open(MESSAGE_FILE, "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception:
        return "No message found. Create message.txt."

@app.route("/")
def index():
    message = read_message()
    html = f"""
    <!doctype html>
    <html>
      <head><meta charset="utf-8"><title>Message</title></head>
      <body style="font-family:Arial; padding:20px;">
        <h1>Message from message.txt</h1>
        <pre style="background:#f4f4f4; padding:10px; border-radius:6px;">{message}</pre>
        <p>Refresh the page after GitHub Action updates <code>message.txt</code>.</p>
      </body>
    </html>
    """
    return Response(html, mimetype="text/html")

if __name__ == "__main__":
    # dev server
    app.run(host="0.0.0.0", port=8000, debug=True)
