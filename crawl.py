from firecrawl import Firecrawl
from bs4 import BeautifulSoup
from readability import Document
from flask import Flask, render_template, url_for, request
import markdown
import os
import requests

app = Flask(__name__)

def toChat(content):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": "Summarize semi-concisely, do not repeat yourself, output in clean markdown format, \n" + content,
            "stream": False
        }
    )

    # Ollama may stream output if not handled, so take only the final response
    data = response.json()
    return data.get("response", "")

def get_HTML(url):
    firecrawl = Firecrawl(api_key="fc-fc23f9fc3b3a47f2a453353a0a5ee51c")
    result = firecrawl.scrape(url, formats=["summary"])
    return result.summary

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            raw_text = get_HTML(url)
            output = toChat(raw_text)
            summary = markdown.markdown(output)
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    