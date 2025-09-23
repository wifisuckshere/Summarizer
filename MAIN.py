from flask import Flask, render_template, request, Response
from app.getHTML import get_HTML
from app.toCHAT import toChat

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/stream", methods=["POST"])
def stream():
    url = request.form.get("url")
    mode = request.form.get("mode")
    if not url:
        return "No URL provided", 400

    raw_text = get_HTML(url)

    if mode == "concise":
        prompt = "Summarize very concisely, focus only on key points, in clean markdown format.\n" + raw_text
    elif mode == "detailed":    
        prompt = "Summarize in detail, covering all important points, in clean markdown format.\n" + raw_text
    else:
        prompt = "Summarize clearly and moderately detailed, in clean markdown format.\n" + raw_text

    return toChat(prompt)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)