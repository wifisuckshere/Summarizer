import requests
from flask import Response
import json
import os


def toChat(prompt):
    def generate():

        ollama_url = os.getenv("OLLAMA_URL")
        ollama_model = os.getenv("OLLAMA_MODEL")

        r = requests.post(
            ollama_url + "/api/generate",
            json={"model": ollama_model, "prompt": prompt, "stream": True},
            stream=True,
        )
        for line in r.iter_lines():
            if not line:
                continue
            try:
                data = json.loads(line.decode("utf-8"))
                if "response" in data:
                    print("CHUNK >>>", data["response"])
                    yield data["response"]
            except:
                pass
    return Response(generate(), mimetype="text/plain")