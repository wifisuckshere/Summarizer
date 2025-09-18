from firecrawl import Firecrawl
from bs4 import BeautifulSoup
from readability import Document
from flask import Flask, render_template, url_for, request
import markdown
import os
import requests

app = Flask(__name__)

def toChat(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,  # use prompt directly
            "stream": False
        }
    )

    data = response.json()
    return data.get("response", "")

def get_HTML(url):
    firecrawl = Firecrawl(api_key="fc-fc23f9fc3b3a47f2a453353a0a5ee51c")
    result = firecrawl.scrape(url, formats=["summary"])
    return result.summary


def clean_output(output):
    soup = BeautifulSoup(output, "html.parser")
    text_only = soup.get_text()
    return markdown.markdown(text_only, extensions=["extra", "sane_lists"])

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
    