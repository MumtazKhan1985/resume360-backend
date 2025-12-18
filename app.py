from flask import Flask, request, send_file
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import io

app = Flask(__name__)

@app.route("/generate-resume", methods=["POST"])
def generate_resume():
    data = request.json

    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    text = c.beginText(40, 800)
    text.setFont("Helvetica", 11)

    text.textLine(data.get("name", ""))
    text.textLine(data.get("title", ""))
    text.textLine("")

    text.textLine("Skills:")
    text.textLine(data.get("skills", ""))
    text.textLine("")

    text.textLine("Experience:")
    text.textLine(data.get("experience", ""))
    text.textLine("")

    text.textLine("Education:")
    text.textLine(data.get("education", ""))

    c.drawText(text)
    c.showPage()
    c.save()

    buffer.seek(0)
    return send_file(
        buffer,
        as_attachment=True,
        download_name="Resume360_Resume.pdf",
        mimetype="application/pdf"
    )

if __name__ == "__main__":
    app.run()