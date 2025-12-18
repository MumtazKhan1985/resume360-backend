from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({
        "status": "ok",
        "message": "Resume360 backend running"
    })

@app.route("/generate-resume", methods=["POST"])
def generate_resume():
    data = request.json
    return jsonify({
        "resume": f"""
{data.get('name', '')}
{data.get('title', '')}

Skills:
{data.get('skills', '')}

Experience:
{data.get('experience', '')}

Education:
{data.get('education', '')}
"""
    })

@app.route("/generate-cover-letter", methods=["POST"])
def generate_cover():
    data = request.json
    return jsonify({
        "cover_letter": f"""
Dear Hiring Manager,

My name is {data.get('name','')} and I am applying for the role of {data.get('job','')}.

Skills: {data.get('skills','')}
Experience: {data.get('experience','')}

Sincerely,
{data.get('name','')}
"""
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)