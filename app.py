from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Resume360 backend is running"

# Railway gunicorn use karta hai, isliye ye optional hai
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)