from flask import Flask, render_template, url_for, request
import os
import requests

from clean import clean_output
from getHTML import get_HTML
from toCHAT import toChat

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    if request.method == "POST":
        url = request.form.get("url")
        mode = request.form.get("mode")

        if url:
            raw_text = get_HTML(url)

            if mode == "concise":
                prompt = "Summarize very concisely, focus only on key points, in clean markdown format.\n" + raw_text
            elif mode == "detailed":
                prompt = "Summarize in detail, covering all important points, in clean markdown format.\n" + raw_text
            else:
                prompt = "Summarize clearly and moderately detailed, in clean markdown format.\n" + raw_text

            output = toChat(prompt)
            summary = clean_output(output)
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    